"""
A 64-bit universally unique identifier.
time (0-47)
node (48-63)
"""

import os
import socket
import struct
from datetime import datetime, timezone
from typing import Optional, Tuple

__author__ = "Sumin Byeon"
__email__ = "suminb@gmail.com"
__version__ = "0.2.0"


def ipv4_to_int(addr: str) -> int:
    """Converts an IPv4 address in a string format to a 32-bit integer."""
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def uuid64_fields(encoded_uuid: int) -> Tuple[float, int]:
    """Returns the timestamp (in seconds) and node ID encoded in a UUID64."""
    return ((encoded_uuid >> 16) / 10000, encoded_uuid & 0xFFFF)


class UUID64:
    def __init__(self, node_id: int):
        self.node_id = node_id

    def issue(self, current_time: Optional[datetime] = None) -> int:
        if current_time is None:
            current_time = datetime.now(timezone.utc)
        time_seq = int(current_time.timestamp() * 10000)

        return int(time_seq << 16 | (self.node_id & 0xFFFF))


def issue(
    current_time: Optional[datetime] = None, node_id: Optional[int] = None
) -> int:
    if node_id is None:
        try:
            host = socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            host = "127.0.0.1"
        local_ip = os.environ.get("IPV4_ADDR", host)
        node_id = ipv4_to_int(local_ip) % (2**16)
    uuid = UUID64(node_id)
    return uuid.issue(current_time)
