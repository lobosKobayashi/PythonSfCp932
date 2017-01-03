# -*- encoding: cp932 -*-
"""'
english:
    PythonSf sfPPOppy
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfPPOppy
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    ���̃t�@�C���̑S�Ẵv���O�����E�R�[�h�� kVerifierLab ���ь������쐬���܂����B
    
    �쐬�҂̏��і{�l�Ɍ����Ă͏��p���p�������Ƃ̗�O������ǉ����āA
    ���̃t�@�C���̃\�[�X�� GPLv3 �Ō��J���܂��B

    2016�N 12�� 28�� ���ь���
'"""

if __name__ == '__main__':
    """'
    '"""
    import sys
    #import pdb; pdb.set_trace()
    # print "Now in __main__"   # to dubug
    if ( (len(sys.argv) == 1)
      or (sys.argv[1] == "-h")
      or (sys.argv[1] == "/?")
    ):
        # command line help
        print (
""" PythonSf pre-processr
-h: help: this message
-fl: execute Python one-liner file specified by an argment with PythonSf
   pre-processing.
     There is the converted Python codes in  _tmC.py at the current
   directory.
-f:  execute Python block codes file specified by an argment with PythonSf
   pre-processing
     There is the converted Python codes in  _tmC.py at the current
   directory.

default: no option and an expression string
"""     )
        exit()

    import pysfOp.vrfyPySfOp as md
    # if argv[1] == "temp.vrf" for "testOp.vrf" the do kVerifier test and return True
    # else return False
    if md.checkFileNameDoTest():
        exit()

    # It is not requested to verify PythonSf actions.
    # Now we parse and calculate a given expression.
    import pysfOp.sfPPrcssrOp as md
    if ( sys.argv[1] == '-f'):
        md.convertFileAndExecute( sys.argv[2])
    elif (sys.argv[1] == '-fl'):
        lstLineAt = open(sys.argv[2], 'r').readlines()
        #print "debug lstLineAt:", lstLineAt
        assert len(lstLineAt) == 1, ("You set a file that is not an one-liner:"
                                    + sys.argv[2]
                                    + ":"
                                    + lstLineAt
                                    + "\n"
                                    )
        md.execLine( lstLineAt[0].strip() )
    else:
        #__execLine( (" ".join(sys.argv[1:])).strip() )
        md.execLine( (" ".join(sys.argv[1:])).strip() )

