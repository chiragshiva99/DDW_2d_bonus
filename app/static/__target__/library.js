// Transcrypt'ed from Python, 2021-09-29 15:20:33
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var gen_random_int = function (number, seed) {
	var thislist = [];
	random.seed (seed);
	for (var i = 0; i < number; i++) {
		thislist.append (i);
	}
	random.shuffle (thislist);
	return thislist;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	var array = gen_random_int (number, seed);
	var array_str = '';
	for (var i of array) {
		array_str += '{}, '.format (i);
	}
	document.getElementById ('generate').innerHTML = array_str;
};
export var sortnumber1 = function () {
	var array_str = document.getElementById ('generate').innerHTML;
	var mylist = [];
	for (var i of array_str) {
		if (i.isdigit ()) {
			var j = int (i);
			mylist.append (j);
		}
	}
	insertion_sort (mylist);
};
export var insertion_sort = function (array) {
	var array_str = '';
	for (var i = 1; i < len (array); i++) {
		var temporary = array [i];
		while (temporary < array [i - 1] && i > 0) {
			array [i] = array [i - 1];
			var i = i - 1;
		}
		array [i] = temporary;
	}
	for (var i of array) {
		array_str += '{}, '.format (i);
	}
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var digits = document.getElementById ('numbers').value;
	if (digits == '') {
		window.alert ('Your textbox is empty');
	}
	for (var i of digits) {
		if (i.isalpha ()) {
			window.alert ('Characters are not accepted, please use numbers');
		}
	}
	var array = digits.py_split (',');
	for (var i = 0; i < len (array); i++) {
		var temp = int (array [i]);
		array [i] = temp;
	}
	insertion_sort (array);
};

//# sourceMappingURL=library.map