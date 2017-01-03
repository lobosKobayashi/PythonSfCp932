# -*- encoding: cp932 -*-
"""'
english:
    PythonSf sfPP.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/
    
    Copyright 2016, Kenji Kobayashi
    All program codes in this file was designed by kVerifierLab Kenji Kobayashi

    I release souce codes in this file under the GPLv3
    with the exception of my commercial uses.

    2016y 12m 28d Kenji Kokbayashi

japanese:
    PythonSf sfPP.py
    https://github.com/lobosKobayashi
    http://lobosKobayashi.github.com/

    Copyright 2016, Kenji Kobayashi
    ���̃t�@�C���̑S�Ẵv���O�����E�R�[�h�� kVerifierLab ���ь������쐬���܂����B
    
    �쐬�҂̏��і{�l�Ɍ����Ă͏��p���p�������Ƃ̗�O������ǉ����āA
    ���̃t�@�C���̃\�[�X�� GPLv3 �Ō��J���܂��B

    2016�N 12�� 28�� ���ь���
'"""

def whatFileEncoding():
    """'
    return platform.system(): if windows OS then cp932 file else utf-8 file
    return "utf-8"          : utf-8 file
    return "cp932"          : cp932 file
    '"""
    import platform
    return platform.system()

if __name__ == '__main__':
    """'
    '"""
    def gnExec():
        from multiprocessing import Process, Queue
        while True:
            q = Queue()
            p = Process(target=execTempConverted, args=(q,))
            p.start()
            rtnValAt = q.get()

            yield rtnValAt

            del p
            del q

    gnExecGlb=gnExec()

    import pysf.sfPPrcssr
    pysf.sfPPrcssr.gnExecGlb = gnExecGlb
    pysf.sfPPrcssr.start()
