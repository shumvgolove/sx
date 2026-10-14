// Written by scripts/ci/packages_release.py from the simplex-chat-libs releases.

export const LIBS_RELEASE = "core-7.1.0.14"

export const ADDON_RELEASE: string | undefined = "nodejs-addon-0a4193a434bc"

export const SHA256: {readonly [asset: string]: string} = {
  "simplex-chat-libs-linux-aarch64.zip": "8aa0599e30ae44042d0b096f304e9feac70ca13156efa4c8c21218b362fd2948",
  "simplex-chat-libs-linux-x86_64-postgres.zip": "660024a28dc7dd1eaf9fd2f3624008bed72e16f0422a499afe45899c25ac79a2",
  "simplex-chat-libs-linux-x86_64.zip": "d7899ac0134cb25a108cf03514edd01367e0268f9f8cc3ea0bccd29f323a2b8d",
  "simplex-chat-libs-macos-aarch64.zip": "8e921d2cfbc13cff70cb3af5a1b2ebc99760618ddd777bfd1f9b487cb34be536",
  "simplex-chat-libs-macos-x86_64.zip": "df5bcf409002d24a0a9bcff3ffe8831e2ac3d47f45d3ef6e9d6d17cacb0d9106",
  "simplex-chat-libs-windows-x86_64.zip": "28acb9350b7c613c09ba3096b69ad4e98f137d489f79e729abd8370223c1cb46",
  "simplex-chat-nodejs-linux-aarch64.node": "3636a82c56c48229e0326fa03d6ceb5c16dd3afbcc1e86337783dc53a7328d67",
  "simplex-chat-nodejs-linux-x86_64.node": "55f3479b03fdb57591179ed730da744f1aa362e7529df55221b60028415746e9",
  "simplex-chat-nodejs-macos-aarch64.node": "113776f4d273cce7072f89b682e8f4a9cf6bc05d847e4854e6e7bc88931e0e64",
  "simplex-chat-nodejs-macos-x86_64.node": "6c6284581cbddef6a5c635d1a049aba15009cb0fe9f6f0c6981d74603dcec4e5",
  "simplex-chat-nodejs-windows-x86_64.node": "14d56a00def98997b8d46910d9c9bd59a7726d7963de9987f01b74b1446a4b62",
}
