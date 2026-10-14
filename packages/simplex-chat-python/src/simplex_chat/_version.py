"""Package version and the simplex-chat-libs release it loads.

Written by scripts/ci/packages_release.py: the release PR bumps the version
and pins new library releases with the SHA-256 of their assets.
"""

__version__ = "7.1.0b6.post7"  # PEP 440 — read by hatchling for wheel metadata
LIBS_RELEASE = "core-7.1.0.14"  # simplex-chat-libs release tag
LIBS_SHA256 = {
    "simplex-chat-libs-linux-aarch64.zip": "8aa0599e30ae44042d0b096f304e9feac70ca13156efa4c8c21218b362fd2948",
    "simplex-chat-libs-linux-x86_64-postgres.zip": "660024a28dc7dd1eaf9fd2f3624008bed72e16f0422a499afe45899c25ac79a2",
    "simplex-chat-libs-linux-x86_64.zip": "d7899ac0134cb25a108cf03514edd01367e0268f9f8cc3ea0bccd29f323a2b8d",
    "simplex-chat-libs-macos-aarch64.zip": "8e921d2cfbc13cff70cb3af5a1b2ebc99760618ddd777bfd1f9b487cb34be536",
    "simplex-chat-libs-macos-x86_64.zip": "df5bcf409002d24a0a9bcff3ffe8831e2ac3d47f45d3ef6e9d6d17cacb0d9106",
    "simplex-chat-libs-windows-x86_64.zip": "28acb9350b7c613c09ba3096b69ad4e98f137d489f79e729abd8370223c1cb46",
}
