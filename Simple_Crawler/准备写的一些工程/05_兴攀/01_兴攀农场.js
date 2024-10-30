/*
小程序：兴攀农场
抓登陆包：https://p.xpfarm.cn/treemp/wx.Login/index，将body中的rawData后面的\都变成\\（手动），然后整个body放进变量,rawData举例如下：
"rawData":"{\\"nickName\\":\\"微信用户\\",\\"gender\\":0,\\"language\\":\\"\\",\\"city\\":\\"\\",\\"province\\":\\"\\",\\"country\\":\\"\\",\\"avatarUrl\\":\\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\\",\\"is_demote\\":true}"
变量XPNCCK='body'多账户换行
定时：一天一次
*/
NAME = "兴攀农场";
VALY = ["XPNCCK"];
CK = "";
LOGS = 0;
usid = 0;

const fs = require("fs"),
      {
  v4: uuidv4
} = require("uuid");

dcfkey = process.env.dcfkey;
dcfhost = process.env.dcfhost;

class Bar {
  constructor(_0x197c1d) {
    this.num = ++usid;
    this.f = "账号 [" + this.num + "] ";
    this.body = _0x197c1d;
  }

  async signIn() {
    this.headers = {
      Authorization: this.Authorization
    };

    let _0x5095c4 = await $.task("post", "https://p.xpfarm.cn/treemp/user.PersonalCenter/addSignIn", this.headers, "{}");

    if (_0x5095c4.code == 1000) {
      console.log("用户：[" + this.num + "]  签到：[" + _0x5095c4.message + "]");
    } else {
      _0x5095c4.code == 10200 ? console.log("用户：[" + this.num + "]  签到：[" + _0x5095c4.message + "]") : console.log("用户：[" + this.num + "]  签到出错：[" + _0x5095c4 + "]");
    }
  }

  async getHomePage() {
    this.headers = {
      Authorization: this.Authorization
    };

    let _0x51927d = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/getHomePage", this.headers, "{}");

    _0x51927d.code == 1000 ? (this.type_name = _0x51927d.data.type_name, this.water_value = parseInt(_0x51927d.data.water_value), this.fertilizer_value = parseInt(_0x51927d.data.fertilizer_value), console.log("用户：[" + this.num + "]  个人信息获取：[" + _0x51927d.message + "]  状态：[" + this.type_name + "]  水滴：[" + this.water_value + "]  肥料：[" + this.fertilizer_value + "]")) : console.log("用户：[" + this.num + "]  个人信息获取出错：[" + _0x51927d + "]");
  }

  async addWater() {
    for (let _0x38db27 = 0; _0x38db27 < this.water_value / 10; _0x38db27++) {
      this.headers = {
        Authorization: this.Authorization
      };

      let _0x3ceacb = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/addWater", this.headers, "{}");

      _0x3ceacb.code == 1000 ? console.log("用户：[" + this.num + "]  第" + (_0x38db27 + 1) + "次浇水：[" + _0x3ceacb.message + "]") : console.log("用户：[" + this.num + "]  第" + (_0x38db27 + 1) + "次浇水出错：[" + _0x3ceacb + "]");
      await $.wait(5000)
    }
  }

  async addFertilizer() {
    for (let _0x526be2 = 0; _0x526be2 < this.fertilizer_value; _0x526be2++) {
      this.headers = {
        Authorization: this.Authorization
      };

      let _0x9476ec = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/addFertilizer", this.headers, "{\"type\":0}");

      _0x9476ec.code == 1000 ? console.log("用户：[" + this.num + "]  第" + (_0x526be2 + 1) + "次施肥：[" + _0x9476ec.message + "]") : console.log("用户：[" + this.num + "]  第" + (_0x526be2 + 1) + "次施肥出错：[" + _0x9476ec + "]");
      await $.wait(5000)
    }
  }

  async getTasks() {
    await this.rwd(1);
    await this.rwd(1);
    await this.rwd(2);
    await this.rwd(2);
    await this.rwd(3);
    await this.rwd(3);
    await this.qdrw();
  }

  async rwd(_0x1a0476) {
    this.headers = {
      Authorization: this.Authorization
    };

    let _0xfb9be7 = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/getTasks", this.headers, "{\"type\":" + _0x1a0476 + "}");

    if (_0xfb9be7.code == 1000) {
      console.log("用户：[" + this.num + "]  任务单获取：[" + _0xfb9be7.message + "]");
      let _0xf176c2 = _0xfb9be7.data;

      for (let _0x480ba5 = 0; _0x480ba5 < _0xf176c2.length; _0x480ba5++) {
        let _0x6a78a9 = _0xf176c2[_0x480ba5].name,
            _0x2eeada = _0xf176c2[_0x480ba5].complete_token,
            _0x240d70 = _0xf176c2[_0x480ba5].id,
            _0x20f0bd = _0xf176c2[_0x480ba5].is_completed;
        _0x20f0bd == 1 ? console.log("用户：[" + this.num + "]  任务：[" + _0x6a78a9 + "]奖励已领取，明天再来吧！") : (console.log("用户：[" + this.num + "]  去完成任务：[" + _0x6a78a9 + "]！"), await this.completeTask(_0x240d70, _0x2eeada, _0x6a78a9), console.log("用户：[" + this.num + "]  任务：[" + _0x6a78a9 + "]已完成，去领取奖励！"), await this.receiveTaskReward(_0x240d70, _0x2eeada, _0x6a78a9));
      }
    } else {
      console.log("用户：[" + this.num + "]  任务单获取出错：[" + _0xfb9be7 + "]");
    }
  }

  async qdrw() {
    this.headers = {
      Authorization: this.Authorization
    };

    let _0x4ea8ed = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/getTasks", this.headers, "{\"type\":4}");

    if (_0x4ea8ed.code == 1000) {
      console.log("用户：[" + this.num + "]  签到任务获取：[" + _0x4ea8ed.message + "]");
      let _0x338505 = _0x4ea8ed.data;

      for (let _0x44f2cf = 0; _0x44f2cf < _0x338505.length; _0x44f2cf++) {
        let _0x317ece = _0x338505[_0x44f2cf].name,
            _0x3c1bdb = _0x338505[_0x44f2cf].complete_token,
            _0x14d904 = _0x338505[_0x44f2cf].id,
            _0x8330b8 = _0x338505[_0x44f2cf].is_completed;
        _0x8330b8 == 1 ? console.log("用户：[" + this.num + "]  任务：[" + _0x317ece + "]奖励已领取，明天再来吧！") : (console.log("用户：[" + this.num + "]  领取签到奖励！"), await this.receiveTaskReward2(_0x14d904, _0x3c1bdb, _0x317ece));
      }
    } else {
      console.log("用户：[" + this.num + "]  任务单获取出错：[" + _0x4ea8ed + "]");
    }
  }

  async completeTask(_0x15b527, _0x5256fa, _0x1113d0) {
    this.headers = {
      Authorization: this.Authorization
    };

    let _0x42c3c4 = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/completeTask", this.headers, "{\"task_id\":" + _0x15b527 + ",\"complete_token\":\"" + _0x5256fa + "\"}");

    if (_0x42c3c4.code == 1000) {
      console.log("用户：[" + this.num + "]  任务：[" + _0x1113d0 + "]  完成：[" + _0x42c3c4.message + "]");
    } else {
      if (_0x42c3c4.code == 10200) {
        console.log("用户：[" + this.num + "]  任务：[" + _0x1113d0 + "]  完成：[" + _0x42c3c4.message + "]");
      } else {
        console.log("用户：[" + this.num + "]  签到出错：[" + _0x42c3c4 + "]");
      }
    }
  }

  async receiveTaskReward(_0x4128ec, _0x19c70c, _0x12f8d3) {
    this.headers = {
      Authorization: this.Authorization
    };

    let _0x391cdb = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward", this.headers, "{\"task_id\":" + _0x4128ec + ",\"complete_token\":\"" + _0x19c70c + "\"}");

    if (_0x391cdb.code == 1000) {
      console.log("用户：[" + this.num + "]  任务：[" + _0x12f8d3 + "]  完成：[" + _0x391cdb.message + "]");
    } else {
      _0x391cdb.code == 10200 ? console.log("用户：[" + this.num + "]  任务：[" + _0x12f8d3 + "]：[" + _0x391cdb.message + "]") : console.log("用户：[" + this.num + "]  签到出错：[" + _0x391cdb + "]");
    }
  }

  async receiveTaskReward2(_0x3d2ce9, _0x59a637, _0x4e5fe3) {
    this.headers = {
      Authorization: this.Authorization
    };
    this.headers["content-type"] = "application/json";

    let _0x34a101 = await $.task("post", "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward", this.headers, "{\"task_id\":" + _0x3d2ce9 + ",\"complete_token\":\"" + _0x59a637 + "\"}");

    if (_0x34a101.code == 1000) {
      console.log("用户：[" + this.num + "]  签到任务：[" + _0x4e5fe3 + "]  完成：[" + _0x34a101.message + "]");
    } else {
      _0x34a101.code == 10200 ? console.log("用户：[" + this.num + "]  签到任务：[" + _0x4e5fe3 + "]：[" + _0x34a101.message + "]") : console.log("用户：[" + this.num + "]  签到出错：[" + _0x34a101 + "]");
    }
  }

  async refreshtoken() {
    let _0x303984 = JSON.stringify(this.body),
        _0x5c8de8 = JSON.parse(_0x303984),
        _0x4672f2 = await $.task("post", "https://p.xpfarm.cn/treemp/wx.Login/index", {}, _0x5c8de8);

    _0x4672f2.code == 1000 ? (this.Authorization = _0x4672f2.data.token, console.log("用户：[" + this.num + "]  刷新token成功，完成任务中..."), this.logs = true) : (console.log("用户：[" + this.num + "]  刷新token失败，请检查ck是否正确"), this.logs = false);
  }

}

$ = DD();
!(async () => {
  console.log(NAME);


    await $.ExamineCookie();

    if ($.cookie_list.length < 21) {
      await $.Multithreading("refreshtoken");

      let _0xeceb40 = $.cookie_list.filter(_0xcc5c4e => _0xcc5c4e.logs == true);

      if (_0xeceb40.length == 0) {
        console.log("Cookie格式错误 或 账号被禁封");
        return;
      } else {
        await $.Multithreading("getHomePage");
        await $.Multithreading("signIn");
        await $.Multithreading("getTasks");
        await $.Multithreading("addWater");
        await $.Multithreading("addFertilizer");
        await $.Multithreading("getHomePage");
      }
    }
})().catch(_0x1710ec => {
  console.log(_0x1710ec);
}).finally(() => {});

function DD() {
  return new class {
    constructor() {
      this.cookie_list = [];
      this.message = "";
      this.CryptoJS = require("crypto-js");
      this.NodeRSA = require("node-rsa");
      this.request = require("request");
      this.Sha_Rsa = require("jsrsasign");
    }

    async Multithreading(_0x483be2, _0x1d4972, _0x3d4278) {
      let _0x2a44ff = [];
      !_0x3d4278 && (_0x3d4278 = 1);

      while (_0x3d4278--) {
        for (let _0x135796 of $.cookie_list) {
          _0x2a44ff.push(_0x135796[_0x483be2](_0x1d4972));
        }
      }

      await Promise.allSettled(_0x2a44ff);
    }

    ExamineCookie() {
      // let _0x590335 = process.env[VALY] || CK,
      let _0x590335 = '{"cloudID":"84_EoaY6BPuJfOL82cGZqnOZi-bK7DbIuIacaOEkl9JjrwrswDcBaolSuCHwlQ","encryptedData":"wk9mKJ924RnPL85uZBYYUnDYF34BBBddng7jm86JsciBYiH2FPDxqHSvQyZEcIXJ0KEIPrIQyg3x5gDFf697GvFeu0E7II1EJ2+zO8dpKC4u1/dh8KL6lrmo5MAqJcCFRrf9iMyNJr4Bps2fZAnzZdu3ufAJlVrMro6LXQrI4IaiKzn6rcq7dQJnCZjhAVEQ+JFbb9rmAOtXNasRmd+a499MKj68HOy205Id8+H0nhPGmAqHhqNitK9TDCg9265cABNWTeT/AVIYxoJ/8IefXd48BjsecMcra9xEBuDXpYId/kpDJ6WnAUoDLysTateC/wAG4cwvA4Ok+tOqs+FuAMLQWnKIRGfLBv3zRS2PMxjQX+UKxcCgIUGYZJTrIVUix5+guIHScT3zvs/tNEK29scTN9VitclvxcrlR2aQoSysrnf5bL73IDZwAO0dNAiP","iv":"k7Ywb42N+70Zbr0qQ5pPqQ==","signature":"0a2a43d15ab45fc77e63ece32a95c5bc6c3895ba","userInfo":{"nickName":"微信用户","gender":0,"language":"","city":"","province":"","country":"","avatarUrl":"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132","is_demote":true},"rawData":"{\\"nickName\\":\\"微信用户\\",\\"gender\\":0,\\"language\\":\\"\\",\\"city\\":\\"\\",\\"province\\":\\"\\",\\"country\\":\\"\\",\\"avatarUrl\\":\\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\\",\\"is_demote\\":true}","errMsg":"getUserProfile:ok","openid":"o4WMG41rENEG3_YmaHSvJj0uJ-4g","unionid":"oT4Cj0zhqmYouiyd5zpHn82jaDUY"}',
          _0x2d8195 = 0;

      if (_0x590335) {
        for (let _0x1cf886 of _0x590335.split("\n").filter(_0x180970 => !!_0x180970)) {
          $.cookie_list.push(new Bar(_0x1cf886));
        }

        _0x2d8195 = $.cookie_list.length;
      } else {
        console.log("\n【" + NAME + "】：未填写变量: " + VALY);
      }

      console.log("【" + NAME + "】");
      console.log("共找到" + _0x2d8195 + "个账号");
      return $.cookie_list;
    }

    task(_0xc80f6b, _0x2cab23, _0x4e53af, _0x32e299, _0x5cc1bf) {
      _0xc80f6b == "delete" ? _0xc80f6b = _0xc80f6b.toUpperCase() : _0xc80f6b = _0xc80f6b;
      _0xc80f6b == "post" && (delete _0x4e53af["content-type"], delete _0x4e53af["Content-type"], delete _0x4e53af["content-Type"], $.safeGet(_0x32e299) ? _0x4e53af["Content-Type"] = "application/json;charset=UTF-8" : _0x4e53af["Content-Type"] = "application/x-www-form-urlencoded", _0x32e299 && (_0x4e53af["Content-Length"] = $.lengthInUtf8Bytes(_0x32e299)));
      _0xc80f6b == "get" && (delete _0x4e53af["content-type"], delete _0x4e53af["Content-type"], delete _0x4e53af["content-Type"], delete _0x4e53af["Content-Length"]);
      _0x4e53af.Host = _0x2cab23.replace("//", "/").split("/")[1];
      return new Promise(async _0x46cce6 => {
        if (_0xc80f6b.indexOf("T") < 0) {
          var _0x21b8e5 = {
            url: _0x2cab23,
            headers: _0x4e53af,
            body: _0x32e299,
            proxy: "http://" + _0x5cc1bf
          };
        } else {
          var _0x21b8e5 = {
            url: _0x2cab23,
            headers: _0x4e53af,
            form: JSON.parse(_0x32e299),
            proxy: "http://" + _0x5cc1bf
          };
        }

        if (!_0x5cc1bf) {
          delete _0x21b8e5.proxy;
        }

        this.request[_0xc80f6b.toLowerCase()](_0x21b8e5, (_0x5db6b9, _0x33746d, _0x2369ec) => {
          try {
            if (_0x2369ec) {
              if (LOGS == 1) {
                console.log("================ 请求 ================");
                console.log(_0x21b8e5);
                console.log("================ 返回 ================");

                if ($.safeGet(_0x2369ec)) {
                  console.log(JSON.parse(_0x2369ec));
                } else {
                  console.log(_0x2369ec);
                }
              }
            }
          } catch (_0x3da5cf) {
            console.log(_0x3da5cf, _0x2cab23 + "\n" + _0x4e53af);
          } finally {
            let _0x1ff197 = "";

            if (!_0x5db6b9) {
              if ($.safeGet(_0x2369ec)) {
                _0x1ff197 = JSON.parse(_0x2369ec);
              } else {
                _0x2369ec.indexOf("/") != -1 && _0x2369ec.indexOf("+") != -1 ? _0x1ff197 = $.decrypts(_0x2369ec) : _0x1ff197 = _0x2369ec;
              }
            } else {
              _0x1ff197 = _0x2cab23 + "   API请求失败，请检查网络重试\n" + _0x5db6b9;
            }

            return _0x46cce6(_0x1ff197);
          }
        });
      });
    }

    async readUUID() {
      const _0xf158e8 = "uuid.txt";
      await $.generateUUID(_0xf158e8);

      try {
        const _0x4ad7ab = fs.readFileSync(_0xf158e8, "utf8"),
              _0x3cd92c = _0x4ad7ab.trim();

        return _0x3cd92c;
      } catch (_0x15f2c9) {
        return null;
      }
    }

    generateUUID(_0x1f9690) {
      if (fs.existsSync(_0x1f9690)) {
        return;
      }

      const _0x1fa673 = uuidv4();

      fs.writeFile(_0x1f9690, _0x1fa673, "utf8", _0x17733c => {
        if (_0x17733c) {
          console.error("写入文件出错: " + _0x17733c.message);
          return;
        }

        console.log("uuid.txt 文件已创建并写入 UUID。");
      });
    }

    async getkami() {
      let _0x5b3c37 = await $.readUUID(),
          _0x3d6a23 = await $.task("get", "http://" + dcfhost + ":5705/query?dcf=" + dcfkey + "&MA=" + _0x5b3c37, {});

      return _0x3d6a23;
    }

    lengthInUtf8Bytes(_0x1e796f) {
      let _0x45bbd5 = encodeURIComponent(_0x1e796f).match(/%[89ABab]/g);

      return _0x1e796f.length + (_0x45bbd5 ? _0x45bbd5.length : 0);
    }

    randomArr(_0x47b958) {
      return _0x47b958[parseInt(Math.random() * _0x47b958.length, 10)];
    }

    wait(_0x1f20e9) {
      return new Promise(_0x4ccc19 => setTimeout(_0x4ccc19, _0x1f20e9));
    }

    time(_0x5847ec) {
      return _0x5847ec == 10 ? Math.round(+new Date() / 1000) : +new Date();
    }

    timenow(_0xd33b8e) {
      let _0x3ed3e7 = new Date();

      if (_0xd33b8e == undefined) {
        let _0x543291 = new Date(),
            _0x29f3fe = _0x543291.getFullYear() + "-",
            _0xa5abc1 = (_0x543291.getMonth() + 1 < 10 ? "0" + (_0x543291.getMonth() + 1) : _0x543291.getMonth() + 1) + "-",
            _0x102170 = _0x543291.getDate() + " ",
            _0x13951d = _0x543291.getHours() + ":",
            _0x502607 = _0x543291.getMinutes() + ":",
            _0x52f0c7 = _0x543291.getSeconds() + 1 < 10 ? "0" + _0x543291.getSeconds() : _0x543291.getSeconds();

        return _0x29f3fe + _0xa5abc1 + _0x102170 + _0x13951d + _0x502607 + _0x52f0c7;
      } else {
        if (_0xd33b8e == 0) {
          return _0x3ed3e7.getFullYear();
        } else {
          if (_0xd33b8e == 1) {
            return _0x3ed3e7.getMonth() + 1 < 10 ? "0" + (_0x3ed3e7.getMonth() + 1) : _0x3ed3e7.getMonth() + 1;
          } else {
            if (_0xd33b8e == 2) {
              return _0x3ed3e7.getDate();
            } else {
              if (_0xd33b8e == 3) {
                return _0x3ed3e7.getHours();
              } else {
                if (_0xd33b8e == 4) {
                  return _0x3ed3e7.getMinutes();
                } else {
                  if (_0xd33b8e == 5) {
                    return _0x3ed3e7.getSeconds() + 1 < 10 ? "0" + _0x3ed3e7.getSeconds() : _0x3ed3e7.getSeconds();
                  }
                }
              }
            }
          }
        }
      }
    }

    safeGet(_0x3c9d6f) {
      try {
        if (typeof JSON.parse(_0x3c9d6f) == "object") {
          return true;
        }
      } catch (_0x3fdf3b) {
        return false;
      }
    }

    SJS(_0x2f9161, _0x5eaf47) {
      if (_0x5eaf47 == 0) {
        let _0x2a4361 = "QWERTYUIOPASDFGHJKLZXCVBNM01234567890123456789",
            _0x51126e = _0x2a4361.length,
            _0x51acaa = "";

        for (let _0x5429cc = 0; _0x5429cc < _0x2f9161; _0x5429cc++) {
          _0x51acaa += _0x2a4361.charAt(Math.floor(Math.random() * _0x51126e));
        }

        return _0x51acaa;
      } else {
        if (_0x5eaf47 == 1) {
          let _0x5d1e21 = "qwertyuiopasdfghjklzxcvbnm0123456789",
              _0x7cb7f6 = _0x5d1e21.length,
              _0x3cf731 = "";

          for (let _0x3be0d3 = 0; _0x3be0d3 < _0x2f9161; _0x3be0d3++) {
            _0x3cf731 += _0x5d1e21.charAt(Math.floor(Math.random() * _0x7cb7f6));
          }

          return _0x3cf731;
        } else {
          let _0x1c270a = "0123456789",
              _0x41742c = _0x1c270a.length,
              _0x21d4d6 = "";

          for (let _0x24dcef = 0; _0x24dcef < _0x2f9161; _0x24dcef++) {
            _0x21d4d6 += _0x1c270a.charAt(Math.floor(Math.random() * _0x41742c));
          }

          return _0x21d4d6;
        }
      }
    }

    udid(_0x512998) {
      function _0x342870() {
        return ((1 + Math.random()) * 65536 | 0).toString(16).substring(1);
      }

      let _0x5ccd3a = _0x342870() + _0x342870() + "-" + _0x342870() + "-" + _0x342870() + "-" + _0x342870() + "-" + _0x342870() + _0x342870() + _0x342870();

      if (_0x512998 == 0) {
        return _0x5ccd3a.toUpperCase();
      } else {
        return _0x5ccd3a.toLowerCase();
      }
    }

    encodeUnicode(_0x568e15) {
      var _0x1c731c = [];

      for (var _0x533ad5 = 0; _0x533ad5 < _0x568e15.length; _0x533ad5++) {
        _0x1c731c[_0x533ad5] = ("00" + _0x568e15.charCodeAt(_0x533ad5).toString(16)).slice(-4);
      }

      return "\\u" + _0x1c731c.join("\\u");
    }

    decodeUnicode(_0x212eeb) {
      _0x212eeb = _0x212eeb.replace(/\\u/g, "%u");
      return unescape(unescape(_0x212eeb));
    }

    RT(_0x4e3c84, _0x32b85a) {
      return Math.round(Math.random() * (_0x32b85a - _0x4e3c84) + _0x4e3c84);
    }

    arrNull(_0x4bca32) {
      var _0xfbfecf = _0x4bca32.filter(_0x64f0a4 => {
        return _0x64f0a4 && _0x64f0a4.trim();
      });

      return _0xfbfecf;
    }

    nowtime() {
      return new Date(new Date().getTime() + new Date().getTimezoneOffset() * 60 * 1000 + 28800000);
    }

    timecs() {
      let _0x376cbd = $.nowtime();

      JSON.stringify(_0x376cbd).indexOf(" ") >= 0 && (_0x376cbd = _0x376cbd.replace(" ", "T"));
      return new Date(_0x376cbd).getTime() - 28800000;
    }

    rtjson(_0x5d7a2e, _0x20e333, _0x290ccd, _0x389170) {
      return _0x389170 == 0 ? JSON.stringify(_0x5d7a2e.split(_0x20e333).reduce((_0x285292, _0x4f201c) => {
        let _0x19140c = _0x4f201c.split(_0x290ccd);

        _0x285292[_0x19140c[0].trim()] = _0x19140c[1].trim();
        return _0x285292;
      }, {})) : _0x5d7a2e.split(_0x20e333).reduce((_0x2952d3, _0x8315b5) => {
        let _0x26f664 = _0x8315b5.split(_0x290ccd);

        _0x2952d3[_0x26f664[0].trim()] = _0x26f664[1].trim();
        return _0x2952d3;
      }, {});
    }

    MD5Encrypt(_0x56fcdd, _0x378ca5) {
      if (_0x56fcdd == 0) {
        return this.CryptoJS.MD5(_0x378ca5).toString().toLowerCase();
      } else {
        if (_0x56fcdd == 1) {
          return this.CryptoJS.MD5(_0x378ca5).toString().toUpperCase();
        } else {
          if (_0x56fcdd == 2) {
            return this.CryptoJS.MD5(_0x378ca5).toString().substring(8, 24).toLowerCase();
          } else {
            if (_0x56fcdd == 3) {
              return this.CryptoJS.MD5(_0x378ca5).toString().substring(8, 24).toUpperCase();
            }
          }
        }
      }
    }

    SHA_Encrypt(_0x2bb914, _0x5da4b1, _0x4bc69c) {
      if (_0x2bb914 == 0) {
        return this.CryptoJS[_0x5da4b1](_0x4bc69c).toString(this.CryptoJS.enc.Base64);
      } else {
        return this.CryptoJS[_0x5da4b1](_0x4bc69c).toString();
      }
    }

    HmacSHA_Encrypt(_0x258513, _0x299050, _0x67b071, _0x2a9e59) {
      return _0x258513 == 0 ? this.CryptoJS[_0x299050](_0x67b071, _0x2a9e59).toString(this.CryptoJS.enc.Base64) : this.CryptoJS[_0x299050](_0x67b071, _0x2a9e59).toString();
    }

    Base64(_0x3af460, _0xd2f424) {
      if (_0x3af460 == 0) {
        return this.CryptoJS.enc.Base64.stringify(this.CryptoJS.enc.Utf8.parse(_0xd2f424));
      } else {
        return this.CryptoJS.enc.Utf8.stringify(this.CryptoJS.enc.Base64.parse(_0xd2f424));
      }
    }

    DecryptCrypto(_0xbd42b7, _0x13aced, _0x186fa0, _0x4d32a4, _0x159af5, _0x258c78, _0x1b0e6b) {
      if (_0xbd42b7 == 0) {
        const _0xdb0a43 = this.CryptoJS[_0x13aced].encrypt(this.CryptoJS.enc.Utf8.parse(_0x159af5), this.CryptoJS.enc.Utf8.parse(_0x258c78), {
          iv: this.CryptoJS.enc.Utf8.parse(_0x1b0e6b),
          mode: this.CryptoJS.mode[_0x186fa0],
          padding: this.CryptoJS.pad[_0x4d32a4]
        });

        return _0xdb0a43.toString();
      } else {
        const _0x2a26aa = this.CryptoJS[_0x13aced].decrypt(_0x159af5, this.CryptoJS.enc.Utf8.parse(_0x258c78), {
          iv: this.CryptoJS.enc.Utf8.parse(_0x1b0e6b),
          mode: this.CryptoJS.mode[_0x186fa0],
          padding: this.CryptoJS.pad[_0x4d32a4]
        });

        return _0x2a26aa.toString(this.CryptoJS.enc.Utf8);
      }
    }

    RSA(_0x2f8cfd, _0x576164) {
      const _0xf82bb1 = require("node-rsa");

      let _0x139e81 = new _0xf82bb1("-----BEGIN PUBLIC KEY-----\n" + _0x576164 + "\n-----END PUBLIC KEY-----");

      _0x139e81.setOptions({
        encryptionScheme: "pkcs1"
      });

      return _0x139e81.encrypt(_0x2f8cfd, "base64", "utf8");
    }

    SHA_RSA(_0x567aaa, _0x1de74d) {
      let _0x20aff9 = this.Sha_Rsa.KEYUTIL.getKey("-----BEGIN PRIVATE KEY-----\n" + $.getNewline(_0x1de74d, 76) + "\n-----END PRIVATE KEY-----"),
          _0x3b73c0 = new this.Sha_Rsa.KJUR.crypto.Signature({
        alg: "SHA256withRSA"
      });

      _0x3b73c0.init(_0x20aff9);

      _0x3b73c0.updateString(_0x567aaa);

      let _0x1fd040 = _0x3b73c0.sign(),
          _0x19f165 = this.Sha_Rsa.hextob64u(_0x1fd040);

      return _0x19f165;
    }

  }();
}