# -*- encoding: cp932 -*-
from __future__ import division
"""'
english:
    PythonSf pysfOp\sfPPrcssrOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf pysfOp\sfPPrcssrOp.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    ���̃t�@�C���̑S�Ẵv���O�����E�R�[�h�� kVerifierLab ���ь������쐬���܂����B
    
    �쐬�҂̏��і{�l�Ɍ����Ă͏��p���p�������Ƃ̗�O������ǉ����āA
    ���̃t�@�C���̃\�[�X�� GPLv3 �Ō��J���܂��B

    2016�N 12�� 28�� ���ь���
'"""

strFileEncodeGlb="cp932"
__all__ = ["execLine"]

def convertGreekLetters(ustrAg):
    dctCnvrtngTbl={     # converting table of Greek Kanji letter to ASCII
            # Larage Greek Letters
            u"��":"k_lAlpha_"
          , u"��":"k_lBeta_"
          , u"��":"k_lGamma_"
          , u"��":"k_lDelta_"
          , u"��":"k_lEpsilon_"
          , u"��":"k_lOZeta_"
          , u"��":"k_lEta_"
          , u"��":"k_lTheta_"
          , u"��":"k_lIota_"
          , u"��":"k_lKappa_"
          , u"��":"k_lLambda_"
          , u"��":"k_lMu_"
          , u"��":"k_lNu_"
          , u"��":"k_lXi_"
          , u"��":"k_lOmicron_"
          , u"��":"k_lPi_"
          , u"��":"k_lRho_"
          , u"��":"k_lSigma_"
          , u"��":"k_lTau_"
          , u"��":"k_lUpsilon_"
          , u"��":"k_lPhi_"
          , u"��":"k_lChi_"
          , u"��":"k_lPsi_"
          , u"��":"k_lOmega_"
    
            # Smallk Greek Letters
          , u"��":"k_sAlpha_"
          , u"��":"k_sBeta_"
          , u"��":"k_sGamma_"
          , u"��":"k_sDelta_"
          , u"��":"k_sEpsilon_"
          , u"��":"k_sZeta_"
          , u"��":"k_sEta_"
          , u"��":"k_sTheta_"
          , u"��":"k_sIota_"
          , u"��":"k_sKappa_"

          , u"��":"lambda"

          , u"��":"k_sMu_"
          , u"��":"k_sNu_"
          , u"��":"k_sXi_"
          , u"��":"k_sOmicron_"
          , u"��":"k_sPi_"
          , u"��":"k_sRho_"
          , u"��":"k_sSigma_"
          , u"��":"k_sTau_"
          , u"��":"k_sUpsilon_"
          , u"��":"k_sPhi_"
          , u"��":"k_sChi_"
          , u"��":"k_sPsi_"
          , u"��":"k_sOmega_"

          , u"`" :"k_bq_"      # back quote
    }

    lstGreekAt = dctCnvrtngTbl.keys()
    ustrAt = u""
    for ch in ustrAg:
        if ch in lstGreekAt:
            ustrAt += dctCnvrtngTbl[ch]
        else:
            ustrAt += ch

    return ustrAt

def convertCaret2Star(ustrAg):
    ustrAt = ustrAg
    # convert ^ to **
    sztAt=0
    while(True):
        sztAt = ustrAt.find('^', sztAt)
        if sztAt == -1: 
            break

        if sztAt>=1 and ustrAt[sztAt-1]=='\\':
            sztAt = sztAt + 1
        else:
            ustrAt = ustrAt[:sztAt]+"**"+ustrAt[sztAt+1:]
            sztAt = sztAt + 2
       
    # convert "\^" to "^"
    sztAt=0
    while(True):
        sztAt = ustrAt.find('^', sztAt)
        if sztAt == -1: 
            return ustrAt
        blAt = (sztAt>=1) and (ustrAt[sztAt-1]=='\\') 
        #if blAt:
        if True:
            ustrAt = ustrAt[:sztAt-1]+"^"+ustrAt[sztAt+1:]            
            sztAt = sztAt
        else:
            sztAt = sztAt + 1

        if sztAt>len(ustrAt):
            assert False

rightSideValueGlb__ = None
def execLine(strAg):
    global rightSideValueGlb__
    try:
        ustrAt = strAg.decode(strFileEncodeGlb)
        ustrAt = convertCaret2Star(ustrAt)
        lstStrAt = ustrAt.split(';')
        wFileAt = open('_tmC.py', 'w')
        usConvertedAt = u""
        usConvertedAt += "# -*- encoding: "+strFileEncodeGlb+" -*-\n"
        usConvertedAt += "from __future__ import division\n"
        usConvertedAt += "from pysfOp.sfFnctnsOp import *\n"
        usConvertedAt += "setDctGlobals(globals())\n"
        usConvertedAt += "from pysfOp.customizeOp import *\n"
        usConvertedAt += "if os.path.exists('./sfCrrntIniOp.py'):\n"
        usConvertedAt += "    from sfCrrntIniOp import *\n"

        #import pdb; pdb.set_trace()
        strLastAt, lstStrAt = lstStrAt[-1], lstStrAt[0:-1]
        for strAt in lstStrAt:
            usConvertedAt += convertGreekLetters(strAt.strip())+"\n"

        strLastAt = strLastAt.strip()
        if "==" in strLastAt:
            pass
        elif "!=" in strLastAt:
            pass
        elif "=" in strLastAt:
            print "Warning! Don't use a assignment sentence in end."
            #strLastAt = strLastAt[strLastAt.rfind('='):]


        if strLastAt == "":
            usConvertedAt += "rightSideValueGlb__ = None\n"
        else:
            usConvertedAt += "rightSideValueGlb__ = "\
                           + convertGreekLetters(strLastAt)+"\n"
            usConvertedAt += 'print "==============================="\n'
            usConvertedAt += "print rightSideValueGlb__"

        usConvertedAt = usConvertedAt.encode(strFileEncodeGlb)
        wFileAt.write(usConvertedAt)
        wFileAt.close()

        exec(usConvertedAt, globals())
        #print "==============================="
        #print rightSideValueGlb__

    except IOError, errValAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit( "IOError:You may use nonexistent variable name:"
                          +str(errValAt) )

    except ValueError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except TypeError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except NameError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except SyntaxError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    except RuntimeError, valAt:
        import traceback
        print traceback.format_exc()
        raise SystemExit (str(valAt) )

    """'
    #except valAt:
    except Exception, valAt:
        if blVrfyAg == True:
            rightSideValueGlb__ =valAt
        else:
            raise SystemExit (str(valAt) )

    '"""
    return rightSideValueGlb__  # vrfyPySfOp.py: __calculateLineString() uses this returned value

def convertFileAndExecute(fileNameAg):
    wFileAt = open('_tmC.py', 'w')
    usConvertedAt = u""
    usConvertedAt += "# -*- encoding: "+strFileEncodeGlb+" -*-\n"
    usConvertedAt += "from __future__ import division\n"
    usConvertedAt += "from pysfOp.sfFnctnsOp import *\n"
    usConvertedAt += "setDctGlobals(globals())\n"
    usConvertedAt += "from pysfOp.customizeOp import *\n"
    usConvertedAt += "if os.path.exists('./sfCrrntIniOp.py'):\n"
    usConvertedAt += "    from sfCrrntIniOp import *\n"

    lstLineAt = open(fileNameAg, 'r').readlines()
    for strAt in lstLineAt:
        strAt = convertCaret2Star(strAt)
        usConvertedAt += convertGreekLetters(strAt.rstrip())+"\n"

    wFileAt.write(usConvertedAt.encode(strFileEncodeGlb))
    wFileAt.close()

    exec(usConvertedAt.encode(strFileEncodeGlb), globals())

"""'
sfPPOp.py "f=�� x:x+1; f(1)"

'"""
