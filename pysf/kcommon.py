# -*- encoding: cp932 -*-
"""'
english:
    PythonSf pysf\kcommon.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysf\kcommon.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    ���̃t�@�C���̑S�Ẵv���O�����E�R�[�h�� kVerifierLab ���ь������쐬���܂����B
    
    �쐬�҂̏��і{�l�Ɍ����Ă͏��p���p�������Ƃ̗�O������ǉ����āA
    ���̃t�@�C���̃\�[�X�� GPLv3 �Ō��J���܂��B

    2016�N 12�� 28�� ���ь���
'"""

from defines import *    # kcommon.varNameInDefine.py �ŃA�N�Z�X�����邽�� import * ���g���܂�



# -------------------- general utility class begin --------------------------------------
def getMax(seqAg, maxAg=0):
    """ �C�� sequence �̍ő�l�����߂܂��B
        maxAg �����́A�s��Ȃǂ̂悤�ȑ��d�V�[�P���X�� max �����߈Ղ����邽�߂ɐ݂��܂���
    """
    for elm in seqAg:
        if elm > maxAg:
            maxAg = elm
    return maxAg

def getMin(seqAg, minAg=0):
    """ �C�� sequence �̍ŏ��l�����߂܂��B
        minAg �����́A�s��Ȃǂ̂悤�ȑ��d�V�[�P���X�� min �����߈Ղ����邽�߂ɐ݂��܂���
    """
    for elm in seqAg:
        if elm < minAg:
            minAg = elm
    return minAg

class ClPair:
    """ sort �\�� Pair �\����
        C++/STL �� pair<T1,T2> �̂悤�Ȃ��̂��~�������܂����Bleft/right �̃y�A�ŊǗ�����
    �f�[�^�\���ł��Bsort �����������Ƃ��́@left ���̃C���X�^���X�� ">" �� "<" ���Z���\
    �ȗv�f�łȂ���΂Ȃ�܂���B
    
        �O�ȏ�̗v�f�̍\���̂����������Ƃ��́A���̃N���X���e���y���[�g���ĕʂɃN���X����
    �������Ă��������B�Ȃ܂� ClPair ���p�����ׂ��ł͂���܂���B�֐��v���O���~���O�̋Z�@��
    ��g����΁A���������o�[�����̃N���X���L�q�ł��邩������܂���B�ł����ɂ͂���Ȕ\�͂�
    ����܂���B�܂������܂ł���K�v���Ȃ��ƍl���܂��B
    """
    def __init__(self, leftAg, rightAg):
        self.left = leftAg
        self.right = rightAg

    def __repr__(self):
        return "(left:"+ str(self.left) + " :: right:" + str(self.right)+')'

    def __cmp__(self, clPairAg):
        if (self.left < clPairAg.left):
            return -1
        elif (self.left > clPairAg.left):
            return 1
        else:
            return 0

class ClError(str):
    def __init__(self, strAg=None):
        str.__init__(strAg)

class kAssertionError:
    def __init__(self, strAg="kAssertionError"):
        self.m_str = strAg
    def __str__(self):
        return self.m_str

def kAssert(blAg, strErrorMessageAg=""):
    """ �߂�l�F�Ȃ�
        ����Ȃ� assert �ł� -O �I�v�V�������g���čœK�������Ƃ��Ȃ��Ȃ��Ă��܂��B�ł�
    ����ł̓��[�U�[�ɏ����G���[����^����Ӗ��� assert ���g������������B���̑΍�
    �Ƃ��āAK.assert(True/False, strErrorMessageAg) ���g���B
    """
    if blAg == False:
        raise kAssertionError(strErrorMessageAg)
    else:
        return

class ClEn:
    def __init__(self, inAg=None):
        self.element=inAg
    def __call__(self, inAg):
        self.element = inAg
    def __eq__(self,inAg):
        return self.element == inAg
    def __ne__(self,inAg):
        return self.element != inAg
    def __int__(self):
        return self.element
    def __str__(self):
        return str(self.element)
    

""" usage and test
class EnWeek(ClEn):
    Sun,Mon,Tus,Wed,Thu,Fri,Sat = range(7)
    Sunday,Monday,Tuseday,Wednesday,Thursday,Friday,Saturday = range(7)

enAt = EnWeek()
enAt(EnWeek.Mon)
print enAt == EnWeek.Mon
"""

class ClEnum:
    """ClEnum(strEnumDeclareration) �ɂ�� C ����ł�  enum instance �𐶐����܂��B
    example: enAt = ClEnum('Sun,Mon,Tus,Wed,Thu,Fri,Sat, \
                            Sunday=1,Monday, Tuseday, Wednesday, Thursday, Friday, Saturday')

            enAt('Sun') # enAt = 'Sun' �ƋL�q�ł��Ȃ��̂��������BPython �̌��E
            if enAt == 'Sunday':.....
            inAt = int(enAt)
    self.lstTpl_in_lstStr = strAg : std::list<pair<int, lst<str> > �ɂ���� enum �f�[�^�^���Ǘ�����
    """
    def __init__(self, arg):
        if isinstance( arg, ClEnum):
            self.strDeclaration = arg.strDeclaration
            self.strAssignedByFunctionalObject = arg.strAssignedByFunctionalObject
            self.lstTpl_in_lstStr = arg.lstTpl_in_lstStr
        elif isinstance( arg, str):
            self.strDeclaration = arg
            self.strAssignedByFunctionalObject = ''
            self.lstTpl_in_lstStr = []

            inEnumFirstValue = 0;
            lstStrAt = [x.strip() for x in arg.split(',')]
            for i, strAt in enumerate(lstStrAt):
                if strAt.find('=') != -1:
                    lstStrAt2 = [x.strip() for x in strAt.split('=')]
                    kAssert(len(lstStrAt2)==2, "Abnormal enum = term:%s" % strAt)
                    inEnumFirstValue = int(lstStrAt2[1])
                    self.lstTpl_in_lstStr.append( (inEnumFirstValue,[]) )
                    strAt=lstStrAt2[0]
                elif i==0:
                    self.lstTpl_in_lstStr.append( (0,[]) )
    
                self.lstTpl_in_lstStr[-1][1].append(strAt)
    
            self.strAssignedByFunctionalObject = self.lstTpl_in_lstStr[0][1][0]
        else:
            assert False, " Abnormal ElEnum __init__  argment:"+ str(arg)
    def __call__(self, strAg):
        for firstValue, lstAt in self.lstTpl_in_lstStr:
            if strAg in lstAt:
                self.strAssignedByFunctionalObject = strAg
                return self
        kAssert(False,"We can't find \"%s\" in declared string list at ClEnum.strDeclaration"% strAg)

    def __eq__(self,strAg):
        if isinstance(strAg, ClEnum):
            return self.__convert2int(self.strAssignedByFunctionalObject)\
                == self.__convert2int(strAg.strAssignedByFunctionalObject)

        if isinstance(strAg, int):
            return self.__convert2int(self.strAssignedByFunctionalObject)\
                == strAg
            
        kAssert(type(strAg) is str,"Abnormal argment:%s at == operator"% strAg\
                + " You must set string argement for ClEnum instace == arigment")
        return self.__convert2int(self.strAssignedByFunctionalObject) == self.__convert2int(strAg)

    def __ne__(self,strAg):
        kAssert(type(strAg) is str,"Abnormal argment:%s at != operator"% strAg\
                + " You must set string argement for ClEnum instace == arigment")
        return self.__convert2int(self.strAssignedByFunctionalObject) != self.__convert2int(strAg)

    def __convert2int(self, strAg):
        """
            ClEnum instance ���ۑ����� enum ���X�g���� strAg �ɑΉ�����l���Ƃ肾���B
        strAg �ɑΉ����镶���� ClEnum instance ��ێ����Ă��Ȃ��Ƃ��� assert error �ɂ���
        """
        for firstValue, lstStrAt in self.lstTpl_in_lstStr:
            if strAg in lstStrAt:
                for i, strAt in enumerate(lstStrAt):
                    if strAg == strAt:
                        return firstValue + i
        kAssert(False,"We can't find \"%s\" in declared string list at ClEnum.__int__"% strAg)

    def __int__(self):
        return self.__convert2int(self.strAssignedByFunctionalObject)
    def __str__(self):
        return self.strAssignedByFunctionalObject +": " + str(self.lstTpl_in_lstStr)

def sort(lstAg):
    """�߂�l lstAt �� sort ���ꂽ����
       lstAt.sort() �̖߂�l�� None �ł���s�ւȂ��ߐ݂���
    """
    lstAt = lstAg
    lstAt.sort()
    return lstAt
# -------------------- general utility class end --------------------------------------

# -------------------- iterator utility begin --------------------------------------
"""
list.reverse() ������
class ClReverse:
    "" Iterator for looping over a sequence backwards
    �Ehttp://www.python.jp/doc/release/tut/node11.html �ɋ@�\�ǉ�
    �Einstanse[...] �� [index] �ŃA�N�Z�X�ł���R���e�i�݂̂��Ώۂł��Bhash container 
      �ɂ͎g���܂���
    �Edef __init__(self, data, sztStartAg=len(data) ) �Ƃ��邱�Ƃ��l���܂�����
      for x in ClReverse(data[sztStart:]) �ƋL�q����Ηǂ����ƂɋC�Â��~�߂܂���
    ""
    def __init__(self, data ):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration     # StopIteration �𓊂��鎖�� iterate ���I�����܂�
        self.index -= 1
#        print self.index   # to debug
        return self.data[self.index]
"""

# -------------------- iterator utility end --------------------------------------

# -------------------- �����񏈗��n utility begin --------------------------------------
""" python �ł̕����񏈗��� find �����s������ -1 ��Ԃ��̂́Alist[-1] �Ɩ�������B���Ԃ�
���X�g�̃}�C�i�X �C���f�b�N�X����Œǉ��������߂̖����ł��傤�B-1 ��Ԃ��̂������� npos
���`���܂��BC++ �� string::npos �Ɠ����悤�Ɏg���܂��B

    sztStartAg �ȂǂɃ}�C�i�X�l�������΁Afind(..) �Ȃǂ̂܂܂� reverse search �ɂ��邱�Ƃ�
�ł��܂��B�ł��A����͕��G�ɂȂ肷���܂��BSTL �Ɏ������܂܂̂ق�����肪���Ȃ��ƍl���܂��B

  �������Anpos �� -1 ��ݒ�ł��܂���Blist[beginSzt:-1] �̈Ӗ��ɂȂ��Ă��܂����Ƃ����邩
��ł��B2**30 �Ƃ��܂��B���̂悤�ɑ傫�ȃT�C�Y�̃V�[�P���X �R���e�i���������Ƃ͂Ȃ��ƍl��
�܂��B
"""
npos = 2**30
def find(lineAg, strFoundAg, sztStartAg=0):
    """ �߂�l: 
        python �� str.find �͌�����Ȃ��Ƃ� -1 ��Ԃ��܂��B����������� npos = 2**30 ��
    �Ԃ� find() �֐���ǉ����܂��Bfind_not_of �Ɠ�������܂�
    """
    sztAt = lineAg.find(strFoundAg,sztStartAg)
    if sztAt == -1:
        return npos
    else:
        return sztAt

def rfind(lineAg, strFoundAg, sztStartAg=0):
    """ �߂�l: 
        python �� str.rfind �͌�����Ȃ��Ƃ� -1 ��Ԃ��܂��B����������� npos = 2**30 ��
    �Ԃ� rfind() �֐���ǉ����܂��Brfind_not_of �Ɠ�������܂�
    """
    sztAt = lineAg.rfind(strFoundAg,sztStartAg)
    if sztAt == -1:
        return npos
    else:
        return sztAt

# 05.10.16 OK
def rfind_first_not_of(strLineAg, strSetAg, sztStartAg=None ):
    """ find_not_of(strLineAg, strSetAg, sztStartAg=None) �� reverse �����ɒT���܂� 
        strSegAg �̒��̕�����������Ȃ��Ƃ��� npos ��Ԃ��܂��B
    """
    if ( sztStartAg is None):
        sztStartAg = len(strLineAg)
    for i, chAt in enumerate(strLineAg[:sztStartAg][::-1]):
        if chAt not in strSetAg:
            return sztStartAg - i

    return npos


def find_first_not_of(cntnrAg, elmAg, sztStartAg=0):
    """ ������̏W�����w�肵�A���̉��ꂩ�ȊO���ŏ��Ɍ����ʒu��T���܂��B
    �Ō�܂Ŏw�肵�������΂���̂Ƃ��� None ��Ԃ��܂��B
    �^����ꂽ strLineAg �̍ŏ��̕����ŕs��v�������������Ƃ��� 0 ��Ԃ��܂��B
    ��v�����΂���̂Ƃ��� npos ��Ԃ��܂��B
        if find_first_not_of(strLineAg,"...") == kcommon.npos : ...
    �Ŕ��肭�������B== 0 �� == None �Ƃ͂��Ȃ��ŉ������B
    """
    if isinstance(cntnrAg,str) or isinstance(cntnrAg,unicode):
        for i, chAt in enumerate(cntnrAg[sztStartAg:]):
            if chAt not in elmAg:
                return i + sztStartAg
    elif isinstance(elmAg,list) or isinstance(elmAg,tuple):
        cntnr = cntnrAg[sztStartAg:]
        for szt, cntnrElm in enumerate(cntnr):
            for elm in elmAg:
                if elm != cntnrElm:
                    return sztStartAg+szt
        return npos
    else:
        cntnr = cntnrAg[sztStartAg:]
        for szt, elm in enumerate(cntnr):
            if elm != elmAg:
                return sztStartAg+szt
        return npos

    return npos

def find_first_of(cntnrAg, elmAg, sztStartAg=0):
    """ �߂�l: elmAg �̉��ꂩ�� cntnrAg ����ŏ��Ɍ����� index �l
        python �� list.index �͌�����Ȃ��Ƃ� ValueError-1 �� throw ���܂��B
    tuple �ł� index ���g���܂���Bstring.find() ��������Ȃ��Ƃ��� -1 ��Ԃ��܂��B
    �����𓝈ꂵ�� stl:find_first_of(.) �̂悤�Ɉ����܂��B
      ..������Ȃ��Ƃ��� npos ��Ԃ��܂�
      ..[arg:] ����`����Ă���V�[�P���X�R���e�i�� == ����`����Ă���v�f��O��Ƃ��܂�
      ..elmAg �ɂ� list, tuple ���F�߂܂�
    """
    if isinstance(cntnrAg,str) or isinstance(cntnrAg,unicode):
        for szt, chAt in enumerate(cntnrAg[sztStartAg:]):
            if chAt in elmAg:
                return szt + sztStartAg
        return npos
    elif isinstance(elmAg,list) or isinstance(elmAg,tuple):
        cntnr = cntnrAg[sztStartAg:]
        for szt, cntnrElm in enumerate(cntnr):
            for elm in elmAg:
                if elm == cntnrElm:
                    return sztStartAg+szt
        return npos
    else:
        cntnr = cntnrAg[sztStartAg:]
        for szt, elm in enumerate(cntnr):
            if elm == elmAg:
                return sztStartAg+szt
        return npos

def searchPairCh( strAg, strBeginEndAg="()",sztStartAg=0,sztEndAg=npos ):
    """ search �֐��̖߂�l (sztStart, sztEnd) �J�n�L���̈ʒu�ƏI���L���̈ʒu�� tuple
    �E'(', ')' �Ȃǂ̈�g�̕����̎n�܂�ƏI�����̈ʒu�����܂��B
    �E�y�A��������Ȃ��Ƃ��� kAssert �G���[�ɂ���
    �E�N���X�ɂ���̂� �J�n�L���^�I���L���̈ʒu�̉�͂����x�������čs���Ƃ��̂��߂ł��B
    // ..[1...[2...]3  ]4   �̕������ chBeginAg=='[', chEndAg==']' �Ƃ����
    // [1 �ɑ΂��� ]4 ��T���o���B���ʂ̑Ή��������邱�Ƃ��ł���B
    �E���������̃y�A�̂Ƃ��̓l�X�e�B���O�𐔂��Ȃ�
    
    """
    assert len(strBeginEndAg)==2, "You must set 2 charactere in strBeginEndAg"
    wdCountBackSlashAt = 0
    wdCountAt = 0
    wdStartAt = 0
    for i, chAt in enumerate(strAg[sztStartAg: sztEndAg]):
        if ( strBeginEndAg[0]==strBeginEndAg[1] and chAt == strBeginEndAg[0]):
            if ( wdCountAt == 0):
                wdStartAt = i + sztStartAg
                wdCountAt = 1
                continue
            else:
                return (wdStartAt, i + sztStartAg)
        
        elif ( strBeginEndAg[0]!=strBeginEndAg[1] and chAt == strBeginEndAg[0]):
            if ( wdCountBackSlashAt % 2 == 0):
                if ( wdCountAt == 0):
                    wdStartAt = i + sztStartAg
                if strBeginEndAg[0] !=  strBeginEndAg[1]:
                    wdCountAt += 1
                
            sztCountBackSlashAt=0
            continue
        elif ( strBeginEndAg[0]!=strBeginEndAg[1] and chAt == strBeginEndAg[1] ):
            if ( wdCountBackSlashAt %2 == 1 ):
                # m_chEnd �����̒��O�Ɋ�� \ �������L��B
                continue
            elif (wdCountAt < 1 ):
                assert False, "Too many End Character:%s" % strBeginEndAg[1]

            elif ( wdCountAt == 1):
                return (wdStartAt, i + sztStartAg)
            
            else:
                if strBeginEndAg[0] !=  strBeginEndAg[1]:
                    wdCountAt -=1;
                continue;
        else:
            if (chAt == '\\' ):
                wdCountBackslashAt+=1;
            else:
                wdCountBackslashAt=0;
            continue;

    if wdCountAt == 0:
        return (npos,npos)
    else:
        return (wdStartAt, npos)

class ClPairedString:
# 05.10.15 OK
    """ search �֐��̖߂�l (sztStart, sztEnd) �J�n�L���̈ʒu�ƏI���L���̈ʒu�� tuple
    �E�y�A��������Ȃ��Ƃ��� kAssert �G���[�ɂ���
       '(', ')' �Ȃǂ̈�g�̕����̎n�܂�ƏI�����̈ʒu�����܂��B
    �E�N���X�ɂ���̂� �J�n�L���^�I���L���̈ʒu�̉�͂����x�������čs���Ƃ��̂��߂ł��B
    // ..[1...[2...]3  ]4   �̕������ chBeginAg=='[', chEndAg==']' �Ƃ����
    // [1 �ɑ΂��� ]4 ��T���o���B���ʂ̑Ή��������邱�Ƃ��ł���B
    // ���̂悤�ɂ������Q�Ƃ��� ..."..."... �̂悤�ɓ��������̃y�A������
    // ���Ȃ��B...a..a...b �� a �Ŏn�܂� b �ŏI���A�l�X�e�B���O�̌��o��
    // ���Ȃ��Ƃ��� ClSimplePaired ���g���B
    """

    def __init__(self, chBeginAg='(', chEndAg=')' ):
        self.m_wdCount=0
        self.m_chBegin=chBeginAg
        self.m_chEnd=chEndAg
        self.wdStart=0
        self.wdCount=0
        self.m_wdCountBackSlash=0
        assert chBeginAg != chEndAg, (
                "Begin Character & End Character are same %s" % chBeginAg)

    def search(self, strAg, wdStartAg=0,wdEndAg=npos ):
        for i, chAt in enumerate(strAg[wdStartAg: wdEndAg]):
            if ( chAt == self.m_chBegin):
                if ( self.m_wdCountBackSlash % 2 == 0):
                    if ( self.m_wdCount == 0):
                        self.m_wdStart = i + wdStartAg
                    self.m_wdCount+= 1
                self.m_wdCountBackSlash=0
                continue
            elif ( chAt == self.m_chEnd ):
                if ( self.m_wdCountBackSlash %2 == 1 ):
                    # m_chEnd �����̒��O�Ɋ�� \ �������L��B
                    continue
                elif (self.m_wdCount < 1 ):
                    assert False, ("Too many End Character:%s" % self.m_chEnd)   #continue # goto Error
                elif ( self.m_wdCount == 1):
                    return (self.m_wdStart, i + wdStartAg)
                
                else:
                    self.m_wdCount-=1;
                    continue;
            else:
                if (chAt == '\\' ):
                    self.m_wdCountBackslash+=1;
                else:
                    m_inCountBackslash=0;
                continue;
        kAssert(False,"We can't find %s %s matched pair"% ( self.m_chBegin, self.m_chEnd) )

# -------------------- �����񏈗��n utility end --------------------------------------

# pico sec ���ŏ��Ƃ��鎞��
# ������ɂ���Ƃ����̌��� 0 �̋�� pS,nS .... TS �܂Ŏ��Ԃ̒P�ʂ�ύX����
class ClTime:
    class EnUnit(ClEn):
        # kVerifier �ɂ��킹�� k_fS �͎g���Ă��܂���
        k_fS,   k_pS, k_nS,k_uS,    k_mS, k_S, k_KS,   k_MS,k_GS,k_TS = range(10)

    def __init__(self, fstAg=0L, sndAg = None):    # inAg �� float ���������
        if isinstance(fstAg, int) or isinstance(fstAg, long):
            if isinstance(sndAg, str):    
                if sndAg == 'k_pS':
                    self.m_ln = fstAg
                elif sndAg == 'k_nS':
                    self.m_ln = fstAg * 10**3
                elif sndAg == 'k_uS':
                    self.m_ln = fstAg * 10**6
                elif sndAg == 'k_mS':
                    self.m_ln = fstAg * 10**9
                elif sndAg == 'k_S':
                    self.m_ln = fstAg * 10**12
                elif sndAg == 'k_KS':
                    self.m_ln = fstAg * 10**15
                elif sndAg == 'k_MS':
                    self.m_ln = fstAg * 10**18
                elif sndAg == 'k_GS':
                    self.m_ln = fstAg * 10**21
                elif sndAg == 'k_TS':
                    self.m_ln = fstAg * 10**24
                else:
                    assert False, "Abnormal ClTime constructor uint string:"+str(sndAg)
            elif (sndAg == None):    
                self.m_ln = long(fstAg)
            else:
                assert False, "Abnormal ClTime constructor second parameter:"+str(sndAg)
        elif isinstance(fstAg, float):
            self.m_dbObserve = fstAg

            import math
            lngAt = 0L
            dbAt = fstAg - math.fmod(fstAg,1e+6);
            lngAt += int( dbAt*10**(+18-6) ) # dbAt �� 10**6 �ȏ�̌��݂̂̐�

            fstAg -= dbAt;
            dbAt = fstAg - math.fmod(fstAg,1e-3);
            lngAt += int( dbAt*10**(3+9) )   # dbAt �� 10**-3 �ȏ�̌��݂̂̐�

            fstAg -= dbAt;                   # inAt �� 10**-3 �ȉ��̐�
            lngAt += int(fstAg*10**12 )       # 
            self.m_ln = lngAt
            
            #print "debug ClTime :", self.m_ln
        elif isinstance(fstAg, ClTime):
            self.m_ln = fstAg.m_ln
        elif (sndAg == None) and isinstance(fstAg, str):
            """ This code is used for time strings and others at the far left 
                in action scripts.
                ----------------- Japanese ----------------------------------
                action scripts �̍��[�ɏ������ +10mS �Ȃǂ̎��������Ɏg���܂�
            """
            fstAg = fstAg.strip()
            assert fstAg[-1] == 'S', "Abnormal ClTime constructor uint string:"+str(fstAg)
            if fstAg[-2] in "pumKMGT":
                strUnitAt = fstAg[-2:]
                strIntAt = fstAg[0:-2]
            else:
                strUnitAt = "S"
                strIntAt = fstAg[0:-1]
            
            strIntAt = strIntAt.strip()
            if strUnitAt == 'pS':
                self.m_ln = long(strIntAt)
            elif strUnitAt == 'nS':
                self.m_ln = long(strIntAt) * 10**3
            elif strUnitAt == 'uS':
                self.m_ln = long(strIntAt) * 10**6
            elif strUnitAt == 'mS':
                self.m_ln = long(strIntAt) * 10**9
            elif strUnitAt == 'S':
                self.m_ln = long(strIntAt) * 10**12
            elif strUnitAt == 'KS':
                self.m_ln = long(strIntAt) * 10**15
            elif strUnitAt == 'MS':
                self.m_ln = long(strIntAt) * 10**18
            elif strUnitAt == 'GS':
                self.m_ln = long(strIntAt) * 10**21
            elif strUnitAt == 'TS':
                self.m_ln = long(strIntAt) * 10**24
            else:
                assert False, "Abnormal ClTime constructor uint string:"+str(fstAg)
        else:
            assert False, str(fstAg) + ": is not integer or float number."

        self.setDouble()

    def SetNextTickTime(self, crTmAg):  # const TyTime& crTmAg
        self.m_ln = crTmAg.m_ln
        self.setDouble()

    def GetTickTime(self):  #return TyTime, const
        return ClTime(self.m_ln)

    def __long__(self):
        return self.m_ln

    def setDouble(self):    # return void
        self.m_dbObserve = 0.0
        # --greater than 1---- less than 1-
        # 999999999,999999,  999 999999999
        inAt    = self.m_ln / 1000000000000   
        inModAt = self.m_ln % 1000000000000
        if ( inAt != 0):
            self.m_dbObserve += inAt

        self.m_dbObserve += float(inModAt)/1000000000000
        

    def GetDouble(self):    # return float
        return self.m_dbObserve;

    def __str__(self):
        #print '__str__ debug:', long(self)
        #print 'debug:', long.__str__(self % 1000)
        # k_fS �� long int �����Ɋ��蓖�ĂĂȂ��̂ŁApS ����n�܂�܂��B
        if (self.m_ln % 1000 != 0):
            return long.__str__(long(self.m_ln))+"pS"
        elif (self.m_ln % 1000**2 != 0):
            # 1000 �̎��� 1000**2 == 1000000 �ł�
            return long.__str__(long(self.m_ln/1000))+"nS"
        elif (self.m_ln % 1000**3 != 0):
            return long.__str__(long(self.m_ln/1000**2))+"uS"
        elif (self.m_ln % 1000**4 != 0):
            return long.__str__(long(self.m_ln/1000**3))+"mS"
        elif (self.m_ln % 1000**5 != 0):
            return long.__str__(long(self.m_ln/1000**4))+"S"
        elif (self.m_ln % 1000**6 != 0):
            return long.__str__(long(self.m_ln/1000**5))+"KS"
        elif (self.m_ln % 1000**7 != 0):
            return long.__str__(long(self.m_ln/1000**6))+"GS"
        else:
            return long.__str__(long(self.m_ln/1000**7))+"TS"

    def __add__(self, objAg):
        lnAt = self.m_ln
        if isinstance(objAg, ClTime):
            lnAt += objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            lnAt += objAg
        elif isinstance(objAg, float):
            lnAt += ClTime(objAg).m_ln
        clAt = ClTime(lnAt)
        clAt.setDouble()
        return clAt

    def __eq__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln == objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln == objAg
        elif isinstance(objAg, float):
            return self.GetDouble == objAg
        else:
            assert False, "Abnorma argment at ClTime:__eq__:" + str(objAg)

    def __gt__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln > objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln > objAg
        elif isinstance(objAg, float):
            return self.GetDouble > objAg
        else:
            assert False, "Abnorma argment at ClTime:__gt__:" + str(objAg)

    def __lt__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln < objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln < objAg
        elif isinstance(objAg, float):
            return self.GetDouble < objAg
        else:
            assert False, "Abnorma argment at ClTime:__lt__:" + str(objAg)

    def __le__(self, objAg):
        if isinstance(objAg, ClTime):
            return self.m_ln <= objAg.m_ln
        elif isinstance(objAg, int) or isinstance(objAg, long):
            return self.m_ln <= objAg
        elif isinstance(objAg, float):
            return self.GetDouble <= objAg
        else:
            assert False, "Abnorma argment at ClTime:__le__:" + str(objAg)

# �߂�l�� enAg �̎�ނɉ��������������_�l
def ConvertEnmTimeToDouble(enAg):   #kc.ClTime.EnUnit �^�C�v�̈���
    if (enAg == ClTime.EnUnit.k_pS ):
        return 1.0e-12
    elif (enAg == ClTime.EnUnit.k_nS ):
        return 1.0e-9
    elif (enAg == ClTime.EnUnit.k_uS ):
        return 1.0e-6
    elif (enAg == ClTime.EnUnit.k_mS ):
        return 1.0e-3
    elif (enAg == ClTime.EnUnit.k_S ):
        return 1.0
    elif (enAg == ClTime.EnUnit.k_KS ):
        return 1.0e3
    elif (enAg == ClTime.EnUnit.k_MS ):
        return 1.0e6
    elif (enAg == ClTime.EnUnit.k_GS ):
        return 1.0e9
    elif (enAg == ClTime.EnUnit.k_TS ):
        return 1.0e12;
    else:
        assert False, "Abnormal enum at ConvertEnmTimeToDouble(.)"

""" ConvertEnmTimeToDouble() �� test
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_pS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_nS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_uS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_mS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_S)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_KS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_MS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_GS)
print ConvertEnmTimeToDouble(ClTime.EnUnit.k_TS)
"""

def ConvertEnmTimeTopCh(enAg): # kc.ClTime.EnUnit �^�C�v�̈���
    if (enAg == ClTime.EnUnit.k_pS ):
        return "pS"
    elif (enAg == ClTime.EnUnit.k_nS ):
        return "nS"
    elif (enAg == ClTime.EnUnit.k_uS ):
        return "uS"
    elif (enAg == ClTime.EnUnit.k_mS ):
        return "mS"
    elif (enAg == ClTime.EnUnit.k_S ):
        return "S"
    elif (enAg == ClTime.EnUnit.k_KS ):
        return "KS"
    elif (enAg == ClTime.EnUnit.k_MS ):
        return "MS"
    elif (enAg == ClTime.EnUnit.k_GS ):
        return "GS"
    elif (enAg == ClTime.EnUnit.k_TS ):
        return "TS"
    else:
        assert False, "Abnormal enum at ConvertEnmTimeToDouble(.)"

""" ConvertEnmTimeTopCh() �� test
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_pS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_nS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_uS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_mS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_S)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_KS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_MS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_GS)
print ConvertEnmTimeTopCh(ClTime.EnUnit.k_TS)
"""


#06.08.31 python �� eof() ���g����悤�ɃN���X��݂���
# read only �݂̂�ΏۂƂ��܂��B
# ����  open() is an alias for file().

class ClReadFile(file):
    def __init__(self, fileNameAg):
        self.m_blEOF = False
        file.__init__(self, fileNameAg, 'r')

    def readline(self): # return line string
        strAt = file.readline(self)
        if not strAt:
            self.m_blEOF = True
        return strAt

    def eof(self):
        return self.m_blEOF

""" ClReadFile class �̃e�X�g
fhAt = ClReadFile('test.txt')
strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()

strAt = fhAt.readline()
print strAt
print fhAt.eof()
"""

cInMaxGlb = 2147483647
ctmMaxGlb = ClTime(999999999999999999999999999) # kVerifier ��������ő厞��


# multiple range generator
def mrng(*args):
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head = range(head)
    elif isinstance(head, tuple):
        head = range(*head)
    if tail:
        for i in head:
            for j in mrng(*tail):
                if isinstance(j, tuple):
                    yield (i,)+j
                else:
                    yield (i, j)
    else:
        for i in head:
            yield i

# �������� �� start, size, stride �����Ő�������
# arithmetic sequence is generated with argment start, size, stride
def arSqnc(startOrSizeAg, sizeAg = None, strideAg=1):
    if sizeAg == None:
        return range(startOrSizeAg)
    else:
        tplAt = ()
        for i in range(sizeAg):
            tplAt += (startOrSizeAg + i*strideAg,)
        return tplAt

# �������̓�������𐶐�����
# generate multiple dimention arithmetic sequence
def masq(*args):
    head, tail = args[0], args[1:]
    if type(head) in [int, long, float]:
        head=range(head)
    elif isinstance(head, tuple) or isinstance(head, list):
        head=arSqnc(*head)
    else:
        kAssert(False, "unexpected argment" + str(args) )

    if tail:
        for i in head:
            for j in masq(*tail):
                if isinstance(j, tuple):
                    yield (i,)+j
                else:
                    yield (i, j)
    else:
        for i in head:
            yield i

# kcommon.dis() ���Ăяo�������W���[���A�N���X���t�A�b�Z���u�����܂�
# dis-assemble the module or class which call kcommon.dis(.)
def dis():
    import dis;import inspect as ins;dis.dis(ins.stack()[1][0].f_code)

#07.08.26 modified from;;http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/65207
# Put in const.py...:
class ClConst(object):
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const(%s)"%name
        self.__dict__[name]=value

# use const.some = 3    # 2 ��ڂ̑���ŃG���[
const = ClConst()
