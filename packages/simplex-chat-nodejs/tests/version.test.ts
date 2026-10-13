import * as fs from "fs"
import * as path from "path"
import {api} from "../src/index"

describe("libsimplex of this change", () => {
  it("reports the cabal version", async () => {
    const dir = fs.mkdtempSync(path.join(__dirname, "tmp-version-"))
    const chat = await api.ChatApi.init({type: "sqlite", filePrefix: path.join(dir, "db")})
    const r: any = await chat.sendChatCmd("/v")
    expect(r.versionInfo.version).toBe("7.1.0.14")
    await chat.close()
    fs.rmSync(dir, {recursive: true, force: true})
  }, 60000)
})
