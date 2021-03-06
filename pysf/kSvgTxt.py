# -*- encoding: cp932 -*-
"""' Text and Arrow SVG generator.
'"""
"""'
english:
Designed by kVerifierLab Kenji Kobayashi;;http://www.nasuinfo.or.jp/FreeSpace/kenji/index.htm

kVerifierLab Kobayashi has the all copyrights in this file. If you consider
comertial use of code(s) in this file, you must informe to kobayashi and
get Kobayshi's consent

kVerifierLab Kobayashi disclose this codes under below QPL license.

Granted Rights

1. You are granted the non-exclusive rights set forth in this license provided you agree to and comply with any and all conditions in this license. Whole or partial distribution of the Software, or software items that link with the Software, in any form signifies acceptance of this license.

2. You may copy and distribute the Software in unmodified form provided that the entire package, including - but not restricted to - copyright, trademark notices and disclaimers, as released by the initial developer of the Software, is distributed.

3. You may make modifications to the Software and distribute your modifications, in a form that is separate from the Software, such as patches. The following restrictions apply to modifications:

a. Modifications must not alter or remove any copyright notices in the Software.
b. When modifications to the Software are released under this license, a non-exclusive royalty-free right is granted to the initial developer of the Software to distribute your modification in future versions of the Software provided such versions remain available under these terms in addition to any other license(s) of the initial developer.

4. You may distribute machine-executable forms of the Software or machine-executable forms of modified versions of the Software, provided that you meet these restrictions:

a. You must include this license document in the distribution.
b. You must ensure that all recipients of the machine-executable forms are also able to receive the complete machine-readable source code to the distributed Software, including all modifications, without any charge beyond the costs of data transfer, and place prominent notices in the distribution explaining this.
c. You must ensure that all modifications included in the machine-executable forms are available under the terms of this license.

5. You may use the original or modified versions of the Software to compile, link and run application programs legally developed by you or by others.

6. You may develop application programs, reusable components and other software items that link with the original or modified versions of the Software. These items, when distributed, are subject to the following requirements:

a. You must ensure that all recipients of machine-executable forms of these items are also able to receive and use the complete machine-readable source code to the items without any charge beyond the costs of data transfer.
b. You must explicitly license all recipients of your items to use and re-distribute original and modified versions of the items in both machine-executable and source code forms. The recipients must be able to do so without any charges whatsoever, and they must be able to re-distribute to anyone they choose.
c. If the items are not available to the general public, and the initial developer of the Software requests a copy of the items, then you must supply one.

Limitations of Liability
In no event shall the initial developers or copyright holders be liable for any damages whatsoever, including - but not restricted to - lost revenue or profits or other direct, indirect, special, incidental or consequential damages, even if they have been advised of the possibility of such damages, except to the extent invariable law, if any, provides otherwise.

No Warranty
The Software and this license document are provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSEｊ.

Choice of Law This license is governed by the Laws of Japan. Disputes shall be settled by Utzunomiya City Court.


japanese:
作成 kVerifierLab 小林;;http://www.nasuinfo.or.jp/FreeSpace/kenji/index.htm

kVerifierLab 小林が、このファイル内にあるプログラム・コード全ての著作権を
保有します。このファイル内のコードを商業利用するときは小林に連絡し、小林の
許諾を得ねばなりません。

kVerifierLab 小林は、下の QPL ライセンスの条件でこのコードを公開します。


許可された権利

1. このライセンスのすべての条件に同意し、従う場合には このライセンスによって産み出される非排他的な以下の権利を 得ることができます。 「ソフトウェア」や「ソフトウェア」をリンクしたソフトウェアを 全体もしくは一部に利用した配布物はどんな形式でも このライセンスを受諾したと見なします。

2. あなたは「ソフトウェア」を、 著作権表示などで制限されていない場合に限り、 オリジナルパッケージが配布されたときのまま変更しない形で 複製、配布することができる。

3. あなたは「ソフトウェア」の変更を行ない、その変更を パッチのように「ソフトウェア」とは独立の形式で配布することができます。 ただし、次のような制限があります。

a. 変更は著作権通知の変更や削除を行なっては行けません。
b. このライセンスに沿って「ソフトウェア」への変更が公開された場合、 「ソフトウェア」の開発者は、 あなたの変更を利用料なしで今後のバージョンで配布することが可能です。 ただし、「ソフトウェア」のライセンスを変更しない場合に限ります。

4. 以下の制限に応じた場合には 「ソフトウェア」の実行形式や 変更された「ソフトウェア」の実行形式の配布が可能です。
a. このライセンス文章を含めて配布しなければなりません。
b. あなたは実行形式を受け取ったすべての人に、 すべての変更を含んだ機械読み取り可能な完全なソースコードを 実費以外のコストをかけずに入手できるように保証しなければなりません。 そして配布物の目立つ場所でこのことを説明しなければなりません。
c. 実行形式に含まれる変更がこのライセンスに従うことを 保証しなければなりません。

5. オリジナル、もしくは変更された「ソフトウェア」を あなたや他の人が開発したアプリケーションプログラムを実行するためにコンパイル・リンクすることができます。

6. オリジナル、もしくは変更された「ソフトウェア」をリンクして アプリケーションプログラムや再利用可能な部品や そのほかのソフトウェアを開発できます。 それらのソフトを配布する場合には次の要求を満たしていなければいけません。
a. それらのソフトウェアの実行形式を受け取ったすべての人に、 機械読み取り可能な完全なソースコードを 実費以外のコストをかけずに入手できるように保証しなければなりません。
b. あなたのソフトウェアを受け取ったすべての人に、 オリジナルのソフトウェアや変更されたソフトウェアの 実行形式やソースコードの再配布や利用するためのライセンスを 明示しなければなりません。 受け取った人は他のどんな料金もなしにそれらが可能でなくてはなりません。 また、他のどんな人にでも再配布可能でなくてはなりません。
c. もしもそのソフトウェアが公衆が利用可能でない場合でも、 「ソフトウェア」の開発者がソフトウェアの複製を要求した場合には その要求に答えなくてはいけません。

責任の制限
どのような場合でも開発者や著作権保持者が 損害に対する責任を負うことはありません。

無保証
「ソフトウェア」とこのライセンスの文章は「そのまま」で「無保証」です。

このライセンスは日本の法律によって保護されています。 争議は宇都宮地裁によって解決されるでしょう。 

'"""
#import sfFnctns as sf
import svgwrite as svg
import numpy as np

class SvSize(object):
    @staticmethod
    def __ConvertToUnicode(strAg):
        if isinstance(strAg, unicode):
            return strAg
        # try convert shift-jis to unicode
        try:
            rtnStr = strAg.decode('shift-jis')
            return rtnStr
        except:
            pass

        # try convert utf-8 to unicode
        try:
            rtnStr = strAg.decode('utf-8')
            return rtnStr
        except:
            pass

        assert False, ("In SvSize::__ConverToUnicodeStr(strAg), we come across "
                     + "unexpected parameter:" + strAg
                      )

    def __init__(self, strAg, flAg=1.0):
        """' data member:m_strUnit, m_flUnit, m_flValue
        '"""
        self.m_strUnit = strAg
        self.m_flUnit = flAg
        if strAg == 'px':
            self.m_flUnit = 1
            self.m_flValue=flAg
        elif strAg == 'mm':
            self.m_flUnit = 1/0.282222229121    # px pixel == 0.282222229121mm
            self.m_flValue = flAg * self.m_flUnit
        elif strAg == 'cm':
            self.m_flUnit = 10/2.82222229121
            self.m_flValue = flAg * self.m_flUnit
        else:
            assert False, "In SvSize.__init__(..) we don't yet implement unit:"+strAg


    def __rmul__(self, flAg):
        assert( isinstance(flAg,(int, float)) ), (
            "In SvSize.__rmul__, you set unexpected value:"+ str(flAg))
        return SvSize(self.m_strUnit, flAg)

    def __mul__(self,ag): #pass      # detect right multiplyer e.g. 17mm*'abc'
        if isinstance(ag, unicode):
            return Text(ag, self)
            #pass
        elif isinstance(ag, Text):
            # not figure out usages yet
            assert False
        elif isinstance(ag, str):
            strAt = SvSize.__ConvertToUnicode(ag)
            return Text(strAt, self)
        else:
            import pdb; pdb.set_trace()
            assert(False)

    def __float__(self):
        return self.m_flValue

    def __int__(self):
        return int(self.m_flValue)


    def __str__(self):
        return str(self.m_flValue)+'px'
        #return str(int(self.m_flValue))

    def getFontPxSize(self):
        inAt = int(self)
        flSize= 2.0*(inAt/2 if inAt%2==0 else (inAt+1)/2)
        return flSize

class P_C_(object):
    """' percent unit class used for margins or positions
    '"""
    def __init__(self):
        self.m_fl=1.0

    def __rmul__(self, flAg):
        assert isinstance(flAg,(int, float))
        self.m_fl=flAg
        return self

    def __mul__(self,ag): #pass      # detect right multiplyer
        return float(self)*ag

    def __float__(self):
        return self.m_fl/100.0

    def __str__(self):
        pass

px=SvSize('px')
mm=SvSize('mm')
cm=SvSize('cm')

#p_c_ = P_C_()
p_c_ = 0.01 # %:p_c_ は単なる数値の方が分かりやすそう。

class Enclosure(object):
    """' Primitive null shape type 
    '"""
    def __init__(self, enclosure=None, insert=None, margin=None):
        """' enclosure==None means there is no element
        enclosre may be lenght 2 nemerical tuple,list, ndarray that define size ndarray
        enclosre may be a pare of size and enclosure object:([1,2], scalable svg instance)
        enclosre may be a enclosured instance which has the data member:m_arSize

        margin may be [left margin, top margin, right margin, bottom margin]
        margin may be [left margin, top margin] # [right margin, bottom margin] is same
        margin may be [value                    # [value,value,value] 

        # できたらいいな:I wish I could
            Enclosure can contain external SVG instance
        '""" 
        def __getNW_SE():
            """' get tuple position pair of NE:north west and SE:south east.
            '"""
            if margin==None:
                arNW = np.array([0,0])
                arSE = np.array([0,0])
            elif hasattr(__len__, margin) and len(margin)==2:
                x,y=float(margin[0]), float(margin[1])
                
                arNW = np.array([x,y])
                arSE = np.array([x,y])
            else:
                assert len(margin) == 4

                x,y=float(margin[0]), float(margin[1])
                arNW = np.array([x,y])

                x,y=float(margin[1]), float(margin[2])
                arSE = np.array([x,y])

            return (arNW,arSE)

        #if  insert != None:
        #    assert np.all(insert==np.array([0,0])) if size==0 else True
        # self.m_arInsert == None means that this has not been deployed yet.
        self.m_arInsert = insert
        self.m_lstMargin=margin
        assert margin==None, 'not implemented m_margin yet'

        if isinstance(enclosure,Enclosure) and hasattr(enclosure,'m_svwObj'):
            # example 17mm"abc" : Text.__init__ has set self.m_arSize, m_svwObje
            arNW,arSE=__getNW_SE()
            self.m_arSize = arNW+enclosure.m_arSize+arSE
            return
        elif isinstance(enclosure,(tuple,list,np.ndarray)) and len(enclosure)==2:
            if isinstance(enclosure[0],(tuple,list,np.ndarray)) and len(enclosure[0])==2:
                # example Enclosure([arSize, 17mm'abc'])
                assert isinstance(enclosure[1], (Enclosure, svg.text.Text))
                if margin==None:
                    arNW = np.array([0,0])
                    arSE = np.array([0,0])
                elif hasattr(__len__, margin) and len(margin)==2:
                    x,y=float(margin[0]), float(margin[1])
                    
                    arNW = np.array([x,y])
                    arSE = np.array([x,y])

                self.m_arSize = np.array(enclosure[0])
                self.m_svwObj = enclosure[1]
                self.m_svwObj.m_arSize=np.array(enclosure[0])
            else:
                # there is no enclosured object. just reserve an arear
                # example: Enclosure([15mm,20mm]), Enclosure(100,200) -- pixel
                arSize=np.array([float(enclosure[0]), float(enclosure[1])])
                arNW,arSE=__getNW_SE()
                self.m_arSize = arNW+arSize+arSE
                self.m_svwObj = None
        elif isinstance(enclosure, Enclosure): 
            #examples: Text(17mm'abc')
            #
            #assert False, "Recursive Enclosure is not implemented yet."
            arNW,arSE=__getNW_SE()
            self.m_arSize = arNW+self.m_arSize+arSE
            self.m_svwObj = self

        else:
            # Empty enclosure which keeps just only an arear.
            assert False

    def __getattr__(self, name):
        # North  East South West, North West, North East, South East, South West
        arInsert = np.array([0,0]) if self.m_arInsert==None else self.m_arInsert
        if np.all(self.m_arSize==[0,0]):
            if name in ('N',"E","S","W","NW","NE","SE","SW","C"):
                return array([0,0]) + arInsert
            elif name == "mt":
                return np.array([[[0,0],[0,0]],[[0,0],[0,0]]]) + arInsert


        if name == "N":                         # North
            return np.array([ arInsert[0]+self.m_arSize[0]/2,
                              arInsert[0]                    ])
        elif name == "E":                       # East
            return np.array([arInsert[0]+self.m_arSize[0]  ,
                             arInsert[1]+self.m_arSize[1]/2])
        elif name == "S":                       # South
            return np.array([arInsert[0]+self.m_arSize[0]/2,
                             arInsert[1]+self.m_arSize[1]  ])
        elif name == "W":                       # West
            return np.array([arInsert[0]                   ,
                             arInsert[1]+self.m_arSize[1]/2])
        elif name == "NW":                      # North West
            return np.array([arInsert[0]                   ,
                             arInsert[1]                   ])
        elif name == "NE":                      # North East
            return np.array([arInsert[0]+self.m_arSize[0]  ,
                             arInsert[1]                   ])
        elif name == "SE":                      # South East
            return mt[1,1]
            return np.array([arInsert[0]+self.m_arSize[0]  ,
                             arInsert[1]+self.m_arSize[1]  ])
        elif name == "SW":                      # South West
            return np.array([arInsert[0]                   ,
                             arInsert[1]+self.m_arSize[1]  ])
        elif name == "C":                       # Center
            return np.array([arInsert[0]+self.m_arSize[0]/2,
                             arInsert[1]+self.m_arSize[1]/2])

        elif name == "mt":
            return np.array([[self.NW, self.NE],
                             [self.SW, self.SE]])

        else:
            raise AttributeError


    class Edge(object):
        """'TBLR:Top, Bottom, Left, Right edge line is Enclosure inner class instance
        which  return np.ndarray posiion on T B L R lines
        example L:start ~[1,1], L:end ~[3,1] then 25p_c_ self.L == ~[1.5,1]
        '""" 
        def __init__(self, ch='T', pos=1/3*p_c_):
                self.m_tplCh_p_c_=(ch,pos)


class Text(Enclosure):
    """' text type which has 4 point positions:up,right,down,left.
    '"""
    @staticmethod
    def getSize(ustrAg, fs, font_family):
        r"""' strAg は ascii text or unicode text 
        We deal with only MS gothic font only because of equal width fonts"

        Cation! Yet not implemented multi lines by \n 
            Also, we should implement, left, middle, right aslignement oprtions
        '"""
        assert fs%2==0
        def __checkHalfSize(ch):
            c=ord(ch)
            if( ( c<=0x7e ) or     # 英数字
                ( c==0xa5 ) or     # \記号
                ( c==0x203e) or    # ~記号
                ( c>=0xff61 and c<=0xff9f)   # 半角カナ
            ):
                return True
            else:
                return False

        n=sum(1 if __checkHalfSize(c) else 2 for c in ustrAg)
        return np.array((fs/2*n, fs))


    def __init__(self, ustrAg, font_size=5*mm, 
                 insert=np.array([0,0]),
                 font_family='MS gothic', **kwd):
        """' font_size is interpreted by the mm size
        kwd are parameters for svgwrite.text.Text.
        '"""
        if isinstance(font_size, int):
            inAt = font_size
            fs= 2.0*(inAt/2 if inAt%2==0 else (inAt+1)/2)
        elif isinstance(font_size, float):
            inAt = int(font_size)
            fs= 2.0*(inAt/2 if inAt%2==0 else (inAt+1)/2)
        elif isinstance(font_size, SvSize):
            fs = font_size.getFontPxSize()
        else:
            assert False, ( 'In Text.__init__, you set a unexpected parameter '
                          + 'for font_size:'+str(font_size)
                          )

        lsUstr=ustrAg.split('\n')
        if len(lsUstr) >= 2:

            cl = InnerMultiLine(lsUstr, fs, insert, font_family, **kwd)
            self.m_arInsert = cl.m_arInsert
            self.m_arSize = cl.m_arSize
            self.m_flFontSize = fs
            self.m_svwObj = cl
        else:
            arSize = Text.getSize(ustrAg, fs, font_family)
            # just only 1 sentence for the time being
            self.m_arInsert=np.array([insert[0], insert[1]+arSize[1]])
            self.m_svwObj=svg.text.Text(ustrAg.encode('utf-8'), font_size=int(fs),
                                insert=self.m_arInsert,
                                font_family=font_family,**kwd)
            self.m_flFontSize=fs
            self.m_arSize=arSize
        
        Enclosure.__init__(self, self, self.m_arInsert)
        self.m_debug=1
    
    def tostring(self, bl_utf_jis=False):
        #import pdb; pdb.set_trace()
        if isinstance(self.m_svwObj, InnerMultiLine):
            return self.m_svwObj.toString(bl_utf_jis, self.m_arInsert)
        else:
            self.m_svwObj['x'],self.m_svwObj['y'] = (
                        int(self.m_arInsert[0]),
                        #int(self.m_arInsert[1]+self.m_flFontSize) 2016.12.27
                        int(self.m_arInsert[1])
                        )
            if bl_utf_jis == True:
                return self.m_svwObj.tostring().encode('utf-8')
            else:
                return self.m_svwObj.tostring().encode('shift-jis')

class InnerMultiLine(Text):
    """' IE11 can't deal with multi line text SVG. So InnerMultiLine behaves multi line text. 
    '"""
    def __init__(self, lsUstrAg, fs, insert, font_family, **kwd):
        widthMax =  0
        self.m_lsSvwObj=[]
        for j, ustrAt in enumerate(lsUstrAg):
            # just only left alignment sentences for the time being
            width = Text.getSize(ustrAt, fs, font_family)[0]
            if width > widthMax:
                widthMax = width

            self.m_lsSvwObj.append( svg.text.Text(ustrAt, font_size=fs,
                                        insert = (insert[0], insert[1]+j*fs ),
                                        font_family = font_family, **kwd)
                                  )

        arSize = np.array([widthMax, len(lsUstrAg) * fs])
        self.m_arInsert = np.array([insert[0], insert[1] + arSize[1]])
        self.m_svwObj = self
        self.m_flFontSize = fs
        self.m_arSize = arSize

    def toString(self, bl_utf_jis, insert):
        strAt=''
        for j,svwAt in enumerate(self.m_lsSvwObj):
            svwAt['x'], svwAt['y'] = (
                        int(insert[0]),
                        int(insert[1]+(j+1)*self.m_flFontSize)
                    )
            if bl_utf_jis == True:
                strAt += svwAt.tostring().encode('utf-8') + u'\n'
            else:
                strAt += svwAt.tostring().encode('shift-jis') + u'\n'

        #strAt = strAt[:-1]      # delete last \n

        return strAt

class AlndEclsAr(Enclosure):
    """'Aligned Enclosure Array

examples
    AlndEclsAr(10mm'ABC', 20mm'→', 10mm'abc').SVG
    '"""
    def __init__(self, mtEcls, lsRow_dx=0, lsCol_dy=0):
        """' mtEcls contains instances of Enclosre
        mtEncls may be np.array(...)

        yet implementted
                may be list or tuple
                may be dictionary with integer index
        '"""
        if isinstance(mtEcls, np.ndarray):
            pass
        else:
            assert False, "At AlndEclsAr.__init__, we presume mtEcls is numpy array for time being."

        tplShape = mtEcls.shape
        if len(tplShape)==1:
            if isinstance(lsRow_dx,(int, float)):
                lsRow_dx=[lsRow_dx]*tplShape[0]
            else:
                assert len(lsRow_dx)==tplShape[0],  ('You set a inappropreate paramter'
                                                    + ' for lsRow_dx:'+str()
                                                    )

            self.m_mtElements = mtEcls

            # Align matrix elements horizontally and vertically
            fnWidth=lambda k: mtEcls[k].E[0]-mtEcls[k].W[0]     # 0:x coordinate
            fnHeight=lambda k: mtEcls[k].S[1]-mtEcls[k].N[1]    # 1:y coordinate
            lsWidth = [fnWidth(k) for k in range(tplShape[0])]
            lsHeight = [fnHeight(k) for k in range(tplShape[0])]
            hrPos = 0   # initialize horizontal position
            flMaxHeight = max(lsHeight)
            for k in range(tplShape[0]):
               mtEcls[k].m_arInsert=np.array([hrPos + lsRow_dx[k]
                                            # ,0.0*(flMaxHeight- lsHeight[k])])
                                            # ,0.25*(flMaxHeight- lsHeight[k])])
                                            # ,0.5*(flMaxHeight- lsHeight[k])])
                                  # ,lsHeight[k]+0.5*(flMaxHeight- lsHeight[k])])
                                            ,0.5*lsHeight[k]+0.5*flMaxHeight])
               hrPos += lsWidth[k]

            self.m_arSize=np.array([mtEcls[-1].m_arInsert[0]
                                        +mtEcls[-1].m_arSize[0], flMaxHeight])
            #Enclosure.__init__(self, self)
            self.m_arInsert = np.array([hrPos, flMaxHeight])
            print "flMaxHeight:",flMaxHeight
            print "lsHeight:",lsHeight
            return

        else:
            assert len(tplShape)==2

            if isinstance(lsRow_dx,(int, float)):
                lsRow_dx=[lsRow_dx]*tplShape[0]
            elif isinstance(lsRow_dx, SvSiz):
                lsRow_dx=[int(lsRow_dx)]*tplShape[0]
            else:
                assert len(lsRow_dx)==tplShape[0],  ('You set a inappropreate paramter'
                                                    + ' for lsRow_dx:'+str()
                                                    )
            if isinstance(lsRow_dy,(int, float)):
                lsRow_dx=[lsRow_dy]*tplShape[1]
            elif isinstance(lsRow_dy, SvSiz):
                lsRow_dx=[int(lsRow_dy)]*tplShape[1]
            else:
                assert len(lsRow_dy)==tplShape[1],  ('You set a inappropreate paramter'
                                                    + ' for lsRow_dy:'+str()
                                                    )

            # Horizontally align matrix elements
            fnWidth=lambda k: max(mtEcls[j,k].E[0]-mtEcls[j,k].W[0] for j in range(tplShape[1]))
            lsMaxWidth = [fnWidth(k) for k in range(tplShape[0])]

            # Vertically align matrix elements
            fnHeight=lambda k: max(mtEcls[k,j].S[1]-mtEcls[k,j].N[1]  for j in range(tplShape[0]))
            lsMaxHeight = [fnHeight(k) for k in range(tplShape[1])]

            for j in range(tplShape[0]):
                for k in range(tplShape[1]):
                    mtEcls[j,k].m_arInsert=np.array([lsMaxWidth[j] + lsRow_dx[k],
                                                     lsMaxHeight[k] + lsRow_dy[k]])

            self.m_mtElements = mtEcls
            self.m_arSize=np.array([sum(lsMaxWidth), sum(lsMaxHeight)])
            Enclosure.__init__(self, self)
            return

    def __getitem__(self,*ag):
        return self.m_mtElements.__getitem__(*ag)
        

    def tostring(self):
        mt = self.m_mtElements
        shape=mt.shape

        strAt=''
        import itertools as it
        for idx in it.product(range(shape[0]), range(shape[1])
                            ) if len(shape)==2 else range(shape[0]):
            if mt[idx] == 0:
                continue

            assert hasattr(mt[idx], 'tostring')

            strAt += mt[idx].tostring()+'\n'
        
        return strAt


class Rect(svg.shapes.Rect, Enclosure):
    def __init__(self, enclosure, margin=[5*p_c_, 10*p_c_, 5*p_c_, 10*p_c_], 
                 size=None, insert=np.array([0,0]),**kwd):
        pass

dwg=None
def show():
    """'save and start'"""
    import os
    dwg.save()
    os.system("start test.svg")

def ksv():
    global dwg, mm
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'), viewBox=('0 0 170 130'))
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'), viewBox=('0 0 170mm 130mm'))
    #dwg = svg.Drawing('test.svg', size=('170mm', '130mm'))
    import sfFnctns as sf
    sf.__getDctGlobals()['mm']=mm

    mm=1/0.282222229121
    # print type(170*mm), 170*mm    # to debug
    dwg = svg.Drawing('test.svg', size=(170*mm, 130*mm))

    sf.__getDctGlobals()['svg']=svg
    sf.__getDctGlobals()['dwg']=dwg

    import kSvgTxt as ksv
    sf.__getDctGlobals()['ksv']=ksv
    return dwg

