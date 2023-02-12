


var s = '`example.com` foo bar `baz`';
var r = s.replace(/`([^`]+)`/g, '<code>$1</code>');
console.log(r);
//=> <code>example.com</code> foo bar <code>baz</code>