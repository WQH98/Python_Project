var _0x9843d3 = function(_0x29d556, _0xcc6df, _0x3d7020) {
    if (0 === _0xcc6df)
        return _0x29d556['substr'](_0x3d7020);
    var _0x48914b;
    _0x48914b = '' + _0x29d556['substr'](0, _0xcc6df);
    return _0x48914b += _0x29d556['substr']((_0xcc6df + _0x3d7020));
};


var shell = function(_0xa0c834) {
    if (!navigator || !navigator['userAgent'])
        return '';

    if ((null == _0xa0c834) || (16 >= _0xa0c834['length']))
        return _0xa0c834;

    var   _0x554c90 = parseInt(_0xa0c834[(_0xa0c834['length'] - 1)], 16) + 9
        , _0x2cf8ae = parseInt(_0xa0c834[_0x554c90], 16);

    _0xa0c834 = _0x9843d3(_0xa0c834, _0x554c90, 1);

    _0x554c90 = _0xa0c834['substr'](_0x2cf8ae, 8);

    _0xa0c834 = _0x9843d3(_0xa0c834, _0x2cf8ae, 8);

    _0x2cf8ae = _grsa_JS['enc']['Utf8']['parse'](_0x554c90);

    _0x554c90 = _grsa_JS['enc']['Utf8']['parse'](_0x554c90);

     _0x554c90 = _grsa_JS['DES']['decrypt']({
         'ciphertext': _grsa_JS['enc']['Hex']['parse'](_0xa0c834)
     }, _0x2cf8ae, {
         'iv': _0x554c90,
         'mode': _grsa_JS['mode']['ECB'],
         'padding': _grsa_JS['pad']['Pkcs7']
     })['toString'](_grsa_JS['enc']['Utf8']);

     return _0x554c90['substring'](0, (_0x554c90['lastIndexOf']('}') + 1));
}
