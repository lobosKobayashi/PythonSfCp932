# -*- encoding: cp932 -*-
"""'
english:
    PythonSf sfCrrntIniOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfCrrntIniOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    ���̃t�@�C���̑S�Ẵv���O�����E�R�[�h�� kVerifierLab ���ь������쐬���܂����B
    
    �쐬�҂̏��і{�l�Ɍ����Ă͏��p���p�������Ƃ̗�O������ǉ����āA
    ���̃t�@�C���̃\�[�X�� GPLv3 �Ō��J���܂��B

    2016�N 12�� 28�� ���ь���
'"""
"""'
python �ł́A�߂�l�� tuple �ɂł���̂ŁA�����̒l��Ԃ����Ƃ��ł���
type ��Ԃ��悤�Ȋ֐��͈���Ȃ����̂Ƃ���
<== instance list/tuple �Ŗ߂�l�� type �Ƃ��Ă���Ƃ���������悤�ɂ��邽�߁B
    <== tuple �l��Ԃ� category function �̖߂�l����̊֐��Ń`�F�b�N���邱�Ƃ�����
        <== m_outType �� length �Ŋm�F�ł���
<== type parameter �Ƃ��� None ��^�����Ƃ��� don&t care ���Ӗ�����
    <== None ���Ԃł��邱�Ƃ����������Ƃ��͏W�� {None} ���g��
<== collection type ���w�肷��Ƃ��� set/frozense �ň����n�����Ƃɂ���
    <== ���͂� {1,2,3} �̃^�C�v�ł��邱�Ƃ� 1 or 2 or 3 �̒l�����^���Ȃ����Ƃ��Ӗ�����
        <== CT �N���X�����ł� frozense �ɂ��Ă��A�ύX���Ȃ����Ƃ𖾋L����
    <== ���̏����ɈӖ����Ȃ����Ƃ���������
    <== �ڎ��� python sf ����Ł@collection type ���w�肵�Ă��邱�Ƃ𖾎��ł���
    <== list/tuple �͕����̓��͈����^tuple �߂�l�ł��邱�Ƃ��Ӗ�������
        <== ��� type list �ň�̓��͈����^��̖߂�l�ł��邱�Ƃ𖾋L���邱�Ƃ�����
        <== ��̊֐��ŕ����̓��́^�o�̓^�C�v�`�F�b�N�����邱�Ƃ��\�ɂ���
    <== CT([1,2,3],[0,1]) �̂悤�� instance sequence �ł̓��o�͌^�w��͋����Ȃ�
        <== z,a,b,c=0,1,2,3; CT([a,b,c],[z,a]) �Ə������Ƃ��A����������ł�
            [a,b,c] �� type �w�肩 instance �w�肩���������Ȃ�����ł�
            <== z,a,b,c=0,1,2,3; CT({a,b,c},{z,a}) �Ə������Ƃ� instance �w��𖾊m�����܂�
            <== ����Ȃ�΁ACT({int,int},{0,1}) �Ȃǂƌ^���̂� instance �Ƃ��ēn�����Ƃ��ł��܂�
<== category �����ł͂Ȃ��A��ʂ� python �֐��ł��g����悤�ɔz������
    <== �L�[����[�h�����̌^�͂ǂ�����
        <== ���ʂ͋l�߂Ȃ�
        <== �����؂�� �����܂ōl������Ȃ�
        <== ��X�炭�ɂ��邽�߂̍l�������͂��Ă����ׂ�
        <== CT �ɓn���i�K�ŃL�[����[�h�܂Ō��܂邱�ƂɂȂ�
            <== CT �̒i�K�ł̓L�[����[�h�����Ɍ^��n���Ă���
            <== �L�[����[�h�����̕�������܂߂��^�t���ƂȂ�
                <== �L�[����[�h�����̕�������܂߂��^�t�������ȂƂ��͕����� CT instace �����
            <==
<== def f(*.sqAg):... �ł��� ���֐��ɂ��^�`�F�b�N�Ȃ�΁A�ϒ������ł����Ă��^�`�F�b�N�𑱂�����
<== �߂葤�̒l�̕����^�`�F�b�N�́A�߂�l�� tuple �̂Ƃ��̂ݍs��
    <== category theory �ł́A�����̌^�̃f�[�^��߂��Ƃ����l�����Ȃ�
        <== �v���O����������ł͗~����
        <== �t�Ɉ�� tuple ��Ԃ��v���O�����������Ȃ��Ȃ�
            <== list ��Ԃ����Ƃő����̏ꍇ�͓�������
<== ���Ƃ��� collection type �͏W����O��Ƃ��Ă���R�[�h�Ɍ�����

���ӁFclass CT �ɂ�����Ainput,outpu �����̃^�C�v�E�`�F�b�N���{���ɐ��������A���Ӑ[���������K�v�ł�
<== metaclass type �� types module �ɓ����Ă��܂���
    <==�ł��E�̎����ʂ��Ă��܂�;; ��x1= fCT(�� x,y:(Z3(1), y),[Z3,Z3],[Z3,Z3]); ��x1(Z3(0),Z3(2))
            if all([type(x) in (types.TypeType, types.ClassType,
                                types.FunctionType,
                                set, frozenset)
                 or isinstance(x, CT)
                 or hasattr(x, '__call__')
                 or isinstance(x, (sf.sc.ndarray,                         ))
                    for x in inputTypeOrSqTypeAg]):

                self.m_tplInType = tuple(inputTypeOrSqTypeAg)

���ϐ��߂�l�ŋ������̂́A�߂�l�̌^�� __len__ method ����������̂����ł��B
    ��F,tuple, list, ndarray                     �̂Ƃ��܂łł�
'"""

"""'
CT; category theory class
    input/output type checking
    ct=CT([int,float],complex); f,g=ct(�� x,y:x+y `i),ct(�� x,y: x y `i); f(3,4.0),g(3, 4.0)
    ===============================
    ((3+4j), 12j)

    ct=CT([int,float],complex); f,g=ct(�� x,y:x+y `i),ct(�� x,y: x y `i); f(3.1,4.0)
    Traceback (most recent call last):
        snipped
    pysf.sfFnctns.ClAppError: Error at CT:__call__(..) input type check:3.1

    CT:__call__(self, fnAg)
        Currying

usage:
    Currying
    ct=CT([Z5,Z5],Z3);f=ct(�� x,y:Z3(x+y)).fst(Z5(3)); f(Z5(1))
    ===============================
    Z3(1)
    f=fCT(�� x,y:Z3(x+y), [Z5,Z5],Z3).fst(Z5(3)); f(Z5(2))
    ===============================
    Z3(0)

'"""
import pysfOp.sfFnctnsOp as sf
#import pysf.octn as oc


def Assert(ag, strAg="at Assert(..)"):
    if ag == False:
        # print strAg   # debug
        raise sf.ClAppError(strAg)
    else:
        return True

import types

class CT(object):
    """' class for typed function and Currying
    ----------------------------------------
    --- Input/Output type check function ---
    ----------------------------------------
    usage:;; ct=CT(int, float); f=ct(�� x: 2.5*x); f(3)
             ct=CT(int, float); f=ct(�� x: 2.5*x); f(3.1)   # AssertError
             ct=CT(int, float); f=ct(�� x: 2  *x); f(3  )   # AssertError
        type check type collection
             f:{0,1,2} --> {0,1,2,3,4,5,6,7,8,9,0}
          collection type(set type in other words) was indicated
        only by a set/frozenset/kfc. You can&t use a tuple or a list.

             ct=CT({0,1,2}, set(range(10))); f=ct(�� x: 2  *x); f(2)
             ct=CT({0,1,2}, set(range(10))); f=ct(�� x: 2  *x); f(3) # input type error
             ct=CT({0,1,2}, set(range(10))); f=ct(�� x: 6  *x); f(2) # output type error

    -------------------------------------------------
    --- Currying functions for first/last argment ---
    -------------------------------------------------
      e.g.
    f=CT()(�� x,y:x+2y).fst(3); f(1),f(2),f(3)
    ===============================
    (5, 7, 9)

    You can use Currying functions without type checks.
    f=CT()(�� x,y:x+y).fst(3); f(1),f(2),f(3)
    ===============================
    (4, 5, 6)
    f=CT()(�� x,y:x+2y).lst(3); f(1),f(2),f(3)
    ===============================
    (7, 8, 9)

    '"""
    def __init__(self, inputTypeOrSqTypeAg=None, outTypeAg=None):
        if inputTypeOrSqTypeAg == None:
            self.m_tplInType = None
        elif isinstance(inputTypeOrSqTypeAg, (tuple, list)):
            # New Type Class:types.TypeType
            # Classical Class:types.ClassType
            if all([type(x) in (types.TypeType, types.ClassType,
                                types.FunctionType,
                                types.NoneType,     # add 2011.11.23
                                set, frozenset)
                 or isinstance(x, CT)
                 or hasattr(x, '__call__')
                 or isinstance(x, (sf.sc.ndarray,                         ))
                    for x in inputTypeOrSqTypeAg]):

                self.m_tplInType = tuple(inputTypeOrSqTypeAg)
            else:
                self.m_tplInType = (tuple(inputTypeOrSqTypeAg), )
        elif isinstance(inputTypeOrSqTypeAg, set):
            self.m_tplInType = (frozenset(inputTypeOrSqTypeAg),)
        else:
            self.m_tplInType = (inputTypeOrSqTypeAg,)
            #self.m_tplInType = inputTypeOrSqTypeAg

        if outTypeAg == None:
            self.m_outType = None
        elif isinstance(outTypeAg, (tuple, list)):
            assert all([type(x) in (types.TypeType, types.ClassType,
                                types.FunctionType,
                                types.NoneType,     # add 2011.11.23
                                set, frozenset)
                 or isinstance(x, CT)
                 or hasattr(x, '__call__')
                 or isinstance(x, (sf.sc.ndarray,                         ))
                                                   for x in outTypeAg])
            self.m_outType = tuple(outTypeAg)
        elif isinstance(outTypeAg, set):
            self.m_outType = (frozenset(outTypeAg),)
        else:
            self.m_outType = (outTypeAg,)
        """'
        if outTypeAg == None:
            self.m_outType = None
        elif isinstance(outTypeAg, (tuple,list)):
            self.m_outType = ( tuple(outTypeAg), )
        else:
            self.m_outType = ( outTypeAg, )
        '"""

    def isType(self, x, tyAg):
        """' Check x is in tyAg. tyAg may be
                a set,list or tuple or
                a function that takes one argment and return a bool value or
                a type e.g. int, float, ... , class or
                any instance that can check == for x
        '"""
        if isinstance(tyAg,  types.NoneType):   # add 2011.11.23
            return True
        elif isinstance(tyAg, (set,sf.sc.ndarray,                         )):
            # tuple, lst, set
            return x in tyAg
        elif isinstance(tyAg, CT):
                assert hasattr(x,'func_name')
                assert hasattr(x,'dom')
                assert hasattr(x,'cod')
                assert x.dom == tyAg.m_tplInType
                assert x.cod == tyAg.m_outType
                return True
        elif type(tyAg) == types.FunctionType:
        #elif hasattr(tyAg,'func_name'):
            # typAg is a function that takes one argment and return a bool value
            return tyAg(x)
        elif type(tyAg) == type or isinstance(tyAg, type):
            # tyAg is a type e.g. int, float, ... , class
            return isinstance(x,tyAg)
        elif isinstance(tyAg, frozenset):
            return x in tyAg
        elif x == tyAg:
            # tyAg is a instance that can check == for x
            return True
        else:
            assert False, ("In isType(..) we have encountered unexpected"
                         + " Object: "+str(tyAg)
                          )

    def __call__(self, fAg):
        """' Instantiate typed function from non typed fAg
            not function composition
        '"""
        def _(*sqAg):
            """' _ is an actual function that checks in/out types
            '"""
            if _.dom == None:
                pass
            elif len(_.dom)==1 and isinstance(_.dom[0], types.FunctionType):
                Assert(_.dom[0](*sqAg),
                        "Error at CT:__call__(..) input type check:"
                        + str(sqAg)
                      )
            elif len(_.dom)==1 and isinstance(_.dom[0], (set, frozenset)):
                    # h=fCT(�� x:x[0],{(1,5),(2,5)}, int); h((1,5)) == 1
                    #  h=fCT(�� x,y:x,{(1,5),(2,5)}, int); h(1,5) ����� assert error.
                    #  <== {(1,5),(2,5)} �ɑ����邱�ƂŌ^���m�F���Ă���A���͈͂�ϐ��֐�
                    Assert(sqAg[0] in _.dom[0],
                            "Error at CT:__call__(..) input type check by set:"
                            + str(sqAg)
                          )
            else:
                assert len(sqAg) == len(_.dom)

                for k in range(len(sqAg)):
                    Assert(self.isType(sqAg[k], _.dom[k]),
                            "Error at CT:__call__(..) input type check:"
                            + str(sqAg[k])
                          )

            valAt = fAg(*sqAg)
            if (_.cod)==None:
                pass
            elif isinstance(valAt, tuple):
            #elif hasattr(valAt, "__len__"):
                if len(_.cod)==1 and isinstance(_.cod[0], types.FunctionType):
                    Assert(_.cod[0](*sqAg),
                            "Error at CT:__call__(..) output type check by function:"
                            + str(valAt)
                          )
                elif len(_.cod)==1 and isinstance(_.cod[0], (set, frozenset)):
                    # h=fCT(�� x:(2,5),int,{(1,5),(2,5)}); h(10) == (2,5)
                    Assert(valAt in _.cod[0],
                            "Error at CT:__call__(..) output type check by set:"
                            + str(valAt)
                          )
                else:
                    assert len(valAt) == len(_.cod)

                    for k in range(len(valAt)):
                        Assert(self.isType(valAt[k], _.cod[k]),
                                "Error at CT:__call__(..) output type check:"
                                + str(valAt[k])
                              )

            else:
                assert len(_.cod) == 1
                Assert(self.isType(valAt, _.cod[0]),
                      "Error at CT:__call__(..) output type check:"
                      + str(valAt)
                      )

            return valAt

        def fst(ag):
            def __(*sqAg):
                return _(*((ag,)+sqAg))

            if _.dom == None:
                return CT()(__)
            else:
                ctAt = CT(_.dom[1:], _.cod)
                return ctAt(__)

        def lst(ag):
            def __(*sqAg):
                return _(*(sqAg+(ag,)))

            if _.dom == None:
                return CT()(__)
            else:
                ctAt = CT(_.dom[:-1], _.cod)
                return ctAt(__)

        _.dom = self.m_tplInType
        _.cod = self.m_outType

        if _.dom == None:
            #if fAg.func_code.co_argcount >= 2:
            #Can't use the upper condition because
            #   (lambda *s:sum(s)).func_code.co_argcount == 0
                _.fst = fst
                _.lst = lst
        elif len(_.dom) >= 2:
            _.fst = fst
            _.lst = lst

        _.f, _.l=fst,lst
        return _

def fCT(f, inputTypeOrSqTypeAg=None, outTypeAg=None):
    # "input/outputTypeorSqTypeAg == None" means "Don't care"
    import copy
    inputTypeOrSqTypeAg = copy.deepcopy(inputTypeOrSqTypeAg)
    outTypeAg = copy.deepcopy(outTypeAg)

    ctAt = CT(inputTypeOrSqTypeAg, outTypeAg)
    return ctAt(f)

def isIF(x):
    return isinstance(x, (int,float))

isN = isIF  # obsolete

def f2CT(f, ty=None, tyOut=None):
    # comment
    if ty==None and tyOut==None:
        return fCT(f,[None,None],tyOut)
    elif ty!=None and tyOut==None:
        return fCT(f, [ty,ty], ty)
    else:
        # ty!=None and tyOut!=None:
        return fCT(f, [ty,ty], tyOut)

def cmps(f,g):
    """' composition of typed functions:f ~* g. f's argemnt must be only 1.
    '"""
    if hasattr(g, '__call__'):
        pass
    else:
        assert hasattr(g, 'func_code') and g.func_code.co_argcount == 1

    if ( hasattr(f, 'dom') and hasattr(g, 'cod')
     and not ((f.dom == None) or (f.dom == (None,))) and not (g.dom == None)
    ):
        assert f.dom == g.cod

        def _(*sqAg):
            if f.func_code.co_argcount > 1:
                return f(*g(*sqAg))
            else:
                return f(g(*sqAg))

        #_.dom = g.dom
        #_.cod = f.cod
        ctAt = CT(g.dom, f.cod)
        return ctAt(_)
    else:
        return lambda *x:f(g(*x))

#k__tilda__UsOp_mul____ = cmps
#k__tilda__UsOp_xor____ = cmps # a ~^ b
#k__tilda__UsOp_mod____ = cmps # a ~% b

#import pysf.octn as oc
# ~* Z5 octonion multiply
#Oc = oc.Oc
#k__tilda__UsOp_mul____ = lambda x,y:Oc(sf.kryO((Oc(x) * Oc(y)).m_tpl, Z5)) # ~*

fAd=flAd=f2CT(lambda x,y:x+y)
fMl=flMl=f2CT(lambda x,y:x*y)

# using algebra related ones
# kfs;  sorted frozenset
# Sb:   substituting Symmetric Group class
# Cy:   make Symmetric Group instance from a cyclic parameter
# extend;make a symmetric group from a set of symmetric group instances or kfs families
# ClZp: Zp(N) class
# TyZp; metaclass for the ClZp to make a pickable Zp(N) instances.
from pysfOp.ptGrpOp import kfs, Cy, extend, group, Sb, TyZp, ClZp, gp
TyZp.N = 2
class Z2(ClZp): pass
TyZp.N = 3
class Z3(ClZp): pass
TyZp.N = 4
class Z4(ClZp): pass
TyZp.N = 5
class Z5(ClZp): pass
TyZp.N = 6
class Z6(ClZp): pass
TyZp.N = 7
class Z7(ClZp): pass
TyZp.N = 257
class Z257(ClZp): pass
ZN = Z257

import pysfOp.octnOp as oc
Oc = oc.Oc

class O2(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, tuple(Z2(x) for x in tplAt))

    def __str__(self):
        return "O2" + super(O2, self).__str__()[2:]

class O3(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, tuple(Z3(x) for x in tplAt))


    def __str__(self):
        return "O3" + super(O3, self).__str__()[2:]

class O4(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, tuple(Z4(x) for x in tplAt))

    def __str__(self):
        return "O4" + super(O4, self).__str__()[2:]

class O5(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, tuple(Z5(x) for x in tplAt))

    def __str__(self):
        return "O5" + super(O5, self).__str__()[2:]

class O6(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, tuple(Z6(x) for x in tplAt))

    def __str__(self):
        return "O6" + super(O6, self).__str__()[2:]

class O7(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, tuple(Z7(x) for x in tplAt))

    def __str__(self):
        return "O7" + super(O7, self).__str__()[2:]

class Ob(Oc):
    def __init__(self, *sqAg):
        if len(sqAg) == 1:
            if hasattr(sqAg[0], '__len__'):
                tplAt = tuple(sqAg[0])
            elif hasattr(sqAg[0], '__getitem__'):
                tplAt = tuple(sqAg[0][:])
            else:
                tplAt = (sqAg[0],)
        else:
            tplAt = tuple(sqAg)

        Oc.__init__(self, sf.kryO(tplAt, ftype=Z257))

    def __str__(self):
        return "Ob" + super(Ob, self).__str__()[2:]

import wave as wv
import numpy as sc
#(nchannels, sampwidth, framerate, nframes, comptype, compname)
__wavePrmsStt = None
def readWv(strFileAg):
    global __wavePrmsStt

    if not( len(strFileAg)>=4 and strFileAg[-4:].upper()=='.WAV'):
        strFileAg = strFileAg + ".wav"

    fileAt = wv.open(strFileAg)
    __wavePrmsStt = fileAt.getparams()
    strAt = fileAt.readframes(__wavePrmsStt[3])
    dataAt = (sc.fromstring(strAt, sc.int16)     )
    return dataAt

def writeWv(vctAg, strFileAg='_tmp.wav'):
    prmAt=__wavePrmsStt
    if not( len(strFileAg)>=4 and strFileAg[-4:].upper()=='.WAV'):
        strFileAg = strFileAg + ".wav"

    fileAt=wv.Wave_write(strFileAg)
    if prmAt == None:
        fileAt.setparams(
                (1, 2, 16000, 32000, 'NONE', 'not compressed'))
    elif isinstance(prmAt, int):
        fileAt.setparams(
                (1, 2, prmAt, 2*pmmAt, 'NONE', 'not compressed'))
    else:
        fileAt.setparams(prmAt)

    if isinstance(vctAg, sc.ndarray) and vctAg.dtype==sc.int16:
        pass
    else:
        vctAg = sc.array(vctAg, dtype=sc.int16)

    fileAt.writeframes(vctAg.tostring())

Fp = lambda Z:sf.kryO__(*[[1,-1/Z],[0,1], object])
Fs = lambda Z:sf.kryO__(*[[1,0],[-Z,1], object])

