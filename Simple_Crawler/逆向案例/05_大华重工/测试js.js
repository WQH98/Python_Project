var arg1 = "1F4EB2D9047FA15831F4DDA6ECCC7E0E3A653301";

var location = { host: "https://www.lydh.com/jituan/" };

document = {}

var _0x4818 = function (arg1) {
  name = "acw_sc__v2";
  var _0x52bd4a = function () {
    var _0x56121a = true;
    return function (_0x215040, _0x309e1a) {
      var _0x23d8c2 = _0x56121a ? function () {
        if (_0x309e1a) {
          var _0x1d7a3f = _0x309e1a["apply"](_0x215040, arguments);

          _0x309e1a = null;
          return _0x1d7a3f;
        }
      } : function () {};

      _0x56121a = false;
      return _0x23d8c2;
    };
  }();

  var _0x1297ed = _0x52bd4a(this, function () {
    var _0x31f094 = function () {
      return "dev";
    },
        _0x114f69 = function () {
      return "window";
    };

    var _0x21d55e = function () {
      var _0x4b4425 = new RegExp("\\w+ *\\(\\) *{\\w+ *['|\"].+['|\"];? *}");

      return !_0x4b4425["test"](_0x31f094["toString"]());
    };

    var _0x2328d0 = function () {
      var _0x56d0ca = new RegExp("(\\\\[x|u](\\w){2,4})+");

      return _0x56d0ca["test"](_0x114f69["toString"]());
    };

    var _0x29c9ca = function (_0x523426) {
      // var _0x17ebab = 0;
      //
      // if (_0x523426["indexOf"](false)) {
      //   _0x442ac7(_0x523426);
      // }
    };

    var _0x442ac7 = function (_0x10471a) {
      // var _0x4d91ed = 3;
      //
      // if (_0x10471a["indexOf"]("true"[3]) !== _0x4d91ed) {
      //   _0x29c9ca(_0x10471a);
      // }
    };

    if (!_0x21d55e()) {
      if (!_0x2328d0()) {
        _0x29c9ca("indеxOf");
      } else {
        _0x29c9ca("indexOf");
      }
    } else {
      _0x29c9ca("indеxOf");
    }
  });

  _0x1297ed();

  var posList = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36];
  var mask = "3000176000856006061501533003690027800375";
  var outPutList = [];
  var arg2 = "";
  var arg3 = "";

  for (var i = 0; i < arg1["length"]; i++) {
    var this_i = arg1[i];

    for (var j = 0; j < posList["length"]; j++) {
      if (posList[j] == i + 1) {
        outPutList[j] = this_i;
      }
    }
  }

  arg2 = outPutList["join"]("");

  for (var i = 0; i < arg2["length"] && i < mask["length"]; i += 2) {
    var strChar = parseInt(arg2["slice"](i, i + 2), 16);
    var maskChar = parseInt(mask["slice"](i, i + 2), 16);
    var xorChar = (strChar ^ maskChar)["toString"](16);

    if (xorChar["length"] == 1) {
      xorChar = "0" + xorChar;
    }

    arg3 += xorChar;
  }

  var expiredate = new Date();
  expiredate["setTime"](expiredate["getTime"]() + 3600000);
  var theHost = location.host,
      theHostSplit = theHost.split("."),
      theHostSplitLength = theHostSplit.length;
  !/^(\d+\.)*\d+$/.test(theHost) && theHostSplitLength > 2 && ("com.cn" != (theHost = theHostSplit[theHostSplitLength - 2] + "." + theHostSplit[theHostSplitLength - 1]) && "gov.cn" != theHost && "org.cn" != theHost && "net.cn" != theHost && "com.my" != theHost || (theHost = theHostSplit[theHostSplitLength - 3] + "." + theHost));
  document["cookie"] = "acw_sc__v2=" + arg3 + ";expires=" + expiredate["toGMTString"]() + ";max-age=3600;path=/" + ";domain=" + theHost;
  return arg3;
};

console.log(_0x4818(arg1));

// document.location.reload();