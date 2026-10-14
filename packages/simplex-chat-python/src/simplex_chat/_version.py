"""Package version and the simplex-chat-libs release it loads.

Written by scripts/ci/packages_release.py: the release PR bumps the version
and pins new library releases with the SHA-256 of their assets.
"""

__version__ = "7.1.0b6.post8"  # PEP 440 — read by hatchling for wheel metadata
LIBS_RELEASE = "core-7.1.0.16"  # simplex-chat-libs release tag
LIBS_SHA256 = {
    "simplex-chat-libs-linux-aarch64.zip": "06a2ac9ee95043b851bae50cd895c67eda3caf12af36ea52fe79a3d951c7ff7a",
    "simplex-chat-libs-linux-x86_64-postgres.zip": "b8890153ed133b7bce149dbf2e05252fccc7e951f7d2451832130873a90ccc49",
    "simplex-chat-libs-linux-x86_64.zip": "97532336dfb291cd4ed65a1209c8166a224b05de67492f1042ff229c12aee7ad",
    "simplex-chat-libs-macos-aarch64.zip": "e7acf8ac176f54cac06e0bcf0476664ccb36566affcab880e098d0c8f21d1f73",
    "simplex-chat-libs-macos-x86_64.zip": "c290e42835b15356b59a683b22d9261d3f7b9d730d81660d99920d6724f99ce2",
    "simplex-chat-libs-windows-x86_64.zip": "8aad135bc54814af367eb60e5802240b1d31c96c40b295703ab2fbb528f8e8e8",
}
