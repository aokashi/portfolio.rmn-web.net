#------------------�ȉ��A�����ݒ荀��-------------------
#�X�̖��O
$title='�V�i�O�_�j�X�N�鍑';

#�Ǘ��Җ��i�����Őݒ肵���Ǘ��Җ��ƃp�X���[�h�ŐV�K�o�^���邱�ƂŁA�Ƃ𖳗��ō쐬���邱�Ƃ��ł��܂��j
$admin_name = '�q�������[';

#�Ǘ��҃p�X���[�h
$admin_pass = '821074';

#���m�点�o�[�@by�܂Ղ� 2008/03/25�@����ɉ���2009/02/07
$news_bar1 =<< "EOM";
<marquee bgcolor=black><font color=red size=4><B>�y����z</font><font color=white size=4>���@�����̏������������ٔ����ł���Ă���܂��B���萔���|�����܂����Ŋ�̍ٔ����ɂď��������肢���܂��B</font></marquee>
EOM
$news_bar2 =<< "EOM";
<marquee bgcolor=black><font color=red size=4><B>�y�o�q�z</font><font color=white size=4>��sA-10�ɂČ��g�S�w����t���I�܂�����ƎQ����낵�����肢���܂��i�L�́M �j�@by���䂤</font></marquee>
EOM
$news_bar3 =<< "EOM";
<marquee bgcolor=black><font color=red size=4><B>�y�A���z</font><font color=white size=4>������ɂ��R���S���܂ŊǗ��l�����܂藈���Ȃ��Ȃ�܂��B������肪����܂����畛�Ǘ��l�y���I�z�y���S�z�ɂ��q�˂��������B</font></marquee>
EOM
#�v���L�V�[��������ю����ȊO���i���h�~�@town_maker.cgi�@�̃z�X�g���� koko2007/09/09
$host_kyuka = 'no';
#�v���L�V�[�����@town_maker.cgi�@
$host_kyuka_meker = 'no';
# �A�N�Z�X�������^�i���p�X�y�[�X�ŋ�؂�j#�v���L�V�[��������ю����ȊO���i���h�~�@#�Ǘ��҃z�X�g��1�@#�Ǘ��҃z�X�g��2������Ă��������B
#  �� ������z�X�g������IP�A�h���X���L�q �D��x��ԁi�A�X�^���X�N�j������g���Ɖ��L�͖�������܂��B
#  �� �L�q�� abc.def.ne.jp 12.34.56.* ���p�X�y�[�X��؂�
$okhost = '';
#�Ǘ��҃z�X�g��1�@'abc.def.ne.jp'�̂悤�Ȏ����̃A�N�Z�X�|�C���g������B���� '*.def.ne.jp'�擪�̂݁u*�v���l�ω��𖳎�
$my_host1 = ''; #*.def.ne.jp
#�Ǘ��҃z�X�g��2�@�@����@��ЂȂǂ̏o�� ������Ă��Ȃ���Ε��ʒʂ�B
$my_host2 = ''; #211.154.120.*
#�����e���t���O�i�ʏ��0�B1�Ń����e���ƂȂ�Q�[���𒆒f�����邱�Ƃ��ł��܂��j
$mente_flag = '0';

#�����e�i���X���̃��b�Z�[�W
$mente_message = '�������܃����e�i���X���B�B�B5�����炢���҂���������';

#�摜�t�H���_�[�iimg�j�̎w��B�v���O��������̑��΃p�X or http://�`����n�܂��΃p�X�@���Ō�́u/�v�͕s�v�ł��B
$img_dir = './img';

#�߂��z�[���y�[�W
$homepage = 'http://w6.oroti.com/~hirarira/';

#�Ǘ��҃��[���A�h���X�i�₢���킹�p�j
$master_ad = '';

#�Ǘ��҃����N#koko2005/09/08
$master_kb = './bbs0/bbs0.cgi';

#�g�b�v��ʂł̂��m�点���e�i�^�O�j
$osirase = <<"EOM";
<!-- ��������-->
<SCRIPT language="JavaScript">
<!--
time=new Date(2006,(7-1),9);
time=Math.ceil((time.getTime()-new Date().getTime())/86400000);
document.write('�^�E�j���[�q�������[�V�e�B�ݒu����A'+-(time)+'���o���܂����B');
//-->
</SCRIPT><br>
<SCRIPT language="JavaScript">
<!--
time=new Date(2006,(9-1),19);
time=Math.ceil((time.getTime()-new Date().getTime())/86400000);
document.write('�q�������[���O���ɂȂ��Ă���A'+-(time)+'���o���܂����B');
//-->
</SCRIPT><br>
<SCRIPT language="JavaScript">
<!--
time=new Date(2007,(7-1),22);
time=Math.ceil((time.getTime()-new Date().getTime())/86400000);
document.write('�V�i�������[�鍑�ɂȂ��Ă���A'+-(time)+'���o���܂����B');
//-->
</SCRIPT><br>
<SCRIPT language="JavaScript">
<!--
time=new Date(2007,(12-1),23);
time=Math.ceil((time.getTime()-new Date().getTime())/86400000);
document.write('�V�i�O�_�j�X�N�鍑�ݗ�����A'+-(time)+'���o���܂����B');
//-->
</SCRIPT><br>
<br>
<INPUT type="button" value="�s�n�v�m�����O���f���A�s�n�v�m�ɓ���Ȃ��o�O���͂������" onclick="parent.location='http://snow.advenbbs.net/bbs/hira.htm';" style="color:#FFFFFF;background:#0000CD;border:1px dotted #000000;"><BR>
<br>
<INPUT type="button" value="�V�i�O�_�j�X�N�鍑���@�A�Z���͕K�������ق��������ł�" onclick="parent.location='keppo.html';" style="color:#FFFFFF;background:#0000CD;border:1px dotted #000000;"><BR>
<br>
<INPUT type="button" value="�V�^�V�i�O�_�j�X�N�鍑�����`���b�g" onclick="parent.location='http://jasin.chatx.whocares.jp/';" style="color:#FFFFFF;background:#009900;border:1px dotted #000000;"><BR>
���������[�U�[��:
<img alt="" width="24" height="12" src="http://jasin.chatx.whocares.jp/mcond/users.png" />  
ROM���[�U�[��:
<img alt="" width="24" height="12" src="http://jasin.chatx.whocares.jp/mcond/roms.png" /><br>
<STYLE TYPE="text/css"><!--BODY {background-image:url("m.gif");background-attachment:fixed;}--></STYLE>
<TEXTAREA cols="85" rows="5" style="background-color:�e�L�X�g�G���A���̔w�i�F;color:�e�L�X�g�G���A���̕����F;">
���̂s�n�v�m�̍X�V����
3��19���@�@�ő�o�^�l��200��250�l��
3��12���@�@�����ɂ�茛�@����
3��11���@�@�ǎ����uSpring�v��
3��9���@�@ �����`���b�g��V�^�֕ύX
2��6���@�@ �d���f���ݒu
2��3���@�@ �X�^���v�����[�̃X�^���v�P��
1�����{�@�@���H�Ɖw�����A���Ȃ��̂�
12��22���@ �ǎ����wWinter�x��
12��21���@ �N���剃��̍��m�J�n
12��18���@ �X�^���v�����[�̃X�^���v�ݒu
11��4���@�@�ǎ����uAutumn�v��
9��9���@�@ �d���o�O�����{��
9��9���@�@ ���[�b�N����p�f���ǉ�
8��29���@�@�K�X���ǉ�
7��29���@�@����TOWN�ǉ�
7��29���@�@���[�b�N���ǉ�
7��22���@�@�ő�o�^�l��175��200�l��
6��29���@�@�uCustomer Floor�v�̃e�X�g�J�n
5��23���@�@�N�����s�ǉ�
5��14���@�@�f�ޒ񋟎Ғǉ�
5��14���@�@�����`���b�g�ݒu
4��5���@�@ �u���C�u�^�E�����łɂ�胊���N���폜
2��29���@�@���[�U�[�폜����50����120����
2��24���@�@�s�n�v�m�����O���f���ݒu
2��24���@�@�o�O�C��
2��19���@�@�V�|�P����TOWN�Ƃ̓�������
2��2���@�@ �C�x���g100���I��
1��5���@�@ �u���C�u�̃o�i�[�����ֈړ�
1��5���@�@ �X�V�������O�_�j�X�N�Ɉړ�����
11��30���@ �����V�X�e������
11��20���@ �u���C�u�^�E���̍L���o�i�[�ݒu
11��10���@ ���@��啝�ɉ���
11��10���@ ���[�b�N�ƒ�s�̔w�i��V�������܂����B
11��3���@�@��s�����̌��E��1���~�ɐݒ�
10��20���@ �劦���ǉ��A�����@�[�g����
9��25���@�@�����@�[�g�����L�����v��
9��25���@�@�[�I�X�g�̖\���ɂ�胉���@�[�g�ƃ��[�b�N�̔���������
8��27���@�@�ő�o�^�l��150��130�l��
8��27���@�@�p�X���[�h����
8��24���@�@���L���̌��x�����Q�T�֑���
8��24���@�@�A�C�e��100��ނقǒǉ�
8��15���@�@�Վ��I���J��
7��31���@�@�X���b�g���R�����ǉ�
7��24���@�@�J�[�h�Q�[���Q�ݒu
7��23���@�@�����̔��@�ݒu
7��23���@�@�V�i�������[�鍑���@���z
7��22���@�@�V�i�������[�鍑�a��
7��22���@�@�q�������[���O������
7��21���@�@�����N�ύX�A���㕛�Ǘ��l�ɂ݂ȂȎ��ɔC��
5��27���@�@�A�C�e���S�R��ނ������ɒǉ��I
4��21���@�@�ő�o�^�l��150��175�l��
4��17���@�@�n�e�e��̃A���ǉ�
4��16���@�@�����������쐬�A������
4��15���@�@�ŋ�����
4��9���@�@ �A�C�e�����e���쐬
4��7���@�@ �M�t�g�쐬���ǉ��I
4��6���@�@ ����̉񕜎��Ԃ�\��
4��3���@�@ �ŋ��@����
4��3���@�@ �ő�o�^�l��130��150�l��
3��30���@�@�����n��i��j�Ɋw�Z�ݗ�
3��30���@�@�n������
3��21���@�@�a�C�Ȃǂ̃R���f�B�V�����啝�ǉ��A�o�O�C��
3��3���@�@ �N�j�i�J�F���X�e�[�V�������F���̑����ցE�E�E�E
1��24���@�@����ύő�o�^�l��150��130�l��
1��24���@�@�����n��i��j�Ɏ�s���ǉ�
1��24���@�@�Ƃ̉��i�A������p����
1��8���@�@ �ő�o�^�l��120��150�l��
12��12���@ ���C���t������
12��11���@ �N�j�i�J�F���X�e�[�V�����u�B�֏��i�v
11��19���@ �ݒ�ύX�A�摜�ǉ�
11��14���@ ���@���z�A�ٔ����ݒu
11��11���@ ���A���O�U���P�T��
11��7���@�@�z���b�N�B�ւ̍q��ւ̉^�s�J�n
11��7���@�@�w�F���B�x���B�ɍ~�i
10��28��   24LIFE�ւ̃����N�ǉ�
10��28���@ k-i��ԏ���
10��22���@ �����n��i��j�ɋ��n��ݗ�
10��22���@ ���L���̌��x��100��20��
10��21���@ �������K��1000�����ނ�100�����ނɕύX
10��11���@ �A�C�e�������ǉ�
10��X���@�@�V��E�E�E�E
9��27���@�@�����K���ύX
9��23���@�@�A�C�e�������ǉ�
9��22���@�@�ő�ő�o�^�l��100�l��120�l��
9��19���@�@�ޓ��@����
9��19���@�@�^�E�j���[�q�������[�V�e�B����q�������[���O��
9��19���@�@�v�v�`�l�^�֘A�Œǉ�
9��16���@�@���[�U�[�폜���Ԃ�20������40���֕ύX
9��15���@�@�ŋ����x����
8��24���@�@�C����ŁA�X�a��
8��23���@�@�^�E�j���[�q�������[�V�e�B�����������{�ݗ�
8��21���@�@�q�������[�����
8��19���@�@�Ɋ����ǉ�
8��18���@�@�ǉ�
8��18���@�@�V�}�b�v�u�Γ��v�ǉ�
8��18���@�@�A�N�Z�T���ǉ�
8��18���@�@�ړ���i��ύX
8��15���@�@�n���n��X�V
8��14���@�@�a�@�A����摜�ύX
8��13���@�@�V�A�C�e���A�V�E�ƕ�W�̒��ӎ����ǉ�
8��12���@�@�X�V����ǉ�</TEXTAREA>
</FORM>
<STYLE TYPE="text/css">
<!--
BODY {background-image:url("Autumn.gif");background-attachment:fixed;}
-->
</STYLE>
<font color=#666666>���Ȃ������̊X�̏Z���ɂȂ��Ă݂܂��񂩁H�@�X�ł͌f����Q�[���Ȃǂ�ʂ��ĐF�X�ȕ��ƒm�荇�������ł��܂��B���܂��܂ȐE�Ƃɂ�����A���؂ȉƂ����Ă���A�ǂ�Ȑl���ɂ��邩�͂��Ȃ�����I���߂Ă̕��͉��́u�V�K�o�^�v���o�^���Ă��������B<br></font>
<font color=#ff6600>����d�o�^�͈ꉞ�����Ă���܂����A����ꍇ�͈ꌾ�Ǘ��҂ɂ��񍐂��������B<br>
���o�^��A���O�̕ύX�͂ł��܂���B</font><br>
<hr>
�摜�A�Z�p�񋟎�<br>
<a href="http://www.propel.ne.jp/~yysky/gallery/" target="_blank"><img src="hakoniwa.gif" border="0"></a>  <a href="http://www.blue-moon.jp/" target="_blank"><img src="ban_s01.jpg" border="0"></a>  <a href="http://www2s.biglobe.ne.jp/~tatsuji/" target="_blank"><img src="tatujibr.gif" border="0"></a>
<hr>
<!-- �����܂�-->
EOM

#�쐬����X�̖��O�i��ԍ��̊X���ŏ��ɕ\�������X�ƂȂ�܂��B��Ƃ��ĂS��ݒ肵�Ă���܂����A�P�����ł��A�S�ȏ�ł��\���܂���B���d�v�F�Q�[���r���ŊX��ǉ�����ꍇ�́A�K���Ō�ɒǉ����Ă��������j
@town_hairetu = ("��s�W���[���X�J","�ՊC�V�s�S�����@�[�g","���[�b�N��","�S�x�X��","�~�T�C���R����","�劦��","����Ȃ��s�X�x���K�X","�閧�s�s�������@�G","�N�����s","���[�b�N��","�K�X��");

#�X�̒n���i��Ŏw�肵���X�̒n���B�����珇�ɏ�ƑΉ�������B�P�ʂ͖��~�j
@town_tika_hairetu = ("10000","1800","500","200","0","10","1600","25000","1000","1000","100");

#�X�̔w�i�X�^�C���i��Ŏw�肵���X�̔w�i�X�^�C���ݒ�B�����珇�ɏ�ƑΉ�������B�X�^�C���ŉ摜�w��j
@page_back = ("background-image : url( img/Spring.png)","background-color:#ffffcc","background-image : url( img/yz.gif)","background-color:#00ffff","background-color:#336699","background-color:#00ccff","background-color:#000000","background-image : url( img/sora.gif)","background-color:#00ff00","background-color:#ffffcc","background-color:#669933");

#�Q���҂����Ă���Ƃ̉摜�Ɖ��i�i'�摜��','���i'�̌`�Őݒ肵�Ă��������B���i�̒P�ʂ́i���~�j�ł��B�Ƃ̉摜��img�t�H���_�ɓ���Ă����K�v������܂��B�j
%ie_hash=('house1.gif','100','house2.gif','100','house3.gif','100','house4.gif','300','house5.gif','300','house6.gif','300','house7.gif','500','house8.gif','500','house9.gif','500','house10.gif','500','house11.gif','800','house12.gif','800','house13.gif','800','house14.gif','800','house15.gif','8000','house16.gif','1000','house17.gif','1000','house18.gif','1000','house19.gif','1000','kamakura.gif','0','bil2.gif','150','bil3.gif','2000','bil4.gif','2000','bil5.gif','2000','sage.gif','2000','bbs6.gif','7777','newhose1.gif','2000','hose99.gif','0','onsen.gif','5000','house20.gif','120000','house21.gif','600000','chip1024.gif','3800000','house23.gif','150000','3r.gif','180000','land5.gif','2000');

#������p�i������A�`D�����N�BA�����N�͂S�̃R���e���c��\���\�AD�����N�͂P�݂̂̃R���e���c��\���\�B�P�ʂ͖��~�j
@housu_nedan = ("2000","1000","500","0");

#����ł̃����L���O�\����
$rankMax='100';

#�����ԐH�����Ȃ��Ǝ���ł��܂����i���[�U�[�폜���ԁj
$deleteUser = '120';

#�H���͉������ƂɂƂ邱�Ƃ��ł��邩
$syokuzi_kankaku = '30';

#�g�̃p���[�̉񕜗��i���b�łP�|�C���g�񕜂��邩�B�������Ȃ��قǉ񕜂������j
$sintai_kaihuku = "5";

#���]�p���[�̉񕜗��i���b�łP�|�C���g�񕜂��邩�B�������Ȃ��قǉ񕜂������j
$zunou_kaihuku = "5";

#���≮�ɕ��ׂ鏤�i�̐�
$orosi_sinakazu = "400";

#���≮�̍݌ɒ����i�usyouhin.dat�v�Ŏw��̍݌ɂ̉��{�̐���u�����B���X�������Ă��Ė≮�̍݌ɐ�������Ȃ��Ǝv�����炱�̐����𑝂₵�Ă��������B1.5�Ȃǂ̎w����j
$ton_zaiko_tyousei = '1';

#�Z���g�����H���ɕ��ׂ�H�i�̎�ސ�
$syokudou_sinakazu = "30";

#�f�p�[�g�ɕ��ׂ鏤�i�̎�ސ�
$depart_sinakazu = "120";

#���L���̌��x��
$syoyuu_gendosuu = '25';

#�H����f�p�[�g�ł̍݌ɒ��ߒl�i��̍݌ɐ������̐����Ŋ����������X���ɕ��т܂��̂ŁA���̐�����傫������قǍ݌ɂ����Ȃ��A����������قǍ݌ɂ������Ȃ�܂��j
$zaiko_tyousetuti ="3";

#���X�̎�ʁi���̃Q�[�����̂��X�ɏo��鏤�i�̃f�[�^�́A�udat_dir�v���ɂ���ushouhin.dat�v�ɋL�^����Ă��܂��B�ushouhin.dat�v�t�@�C���̈�ԍ��ɂ���̂����i��ʂŁA�����́u���X�̎�ʁv�ƑΉ����Ă���K�v������܂��B���������H����\���u�H�v�́ushouhin.dat�v�݂̂ɂ����ʂƂȂ�܂��j
@global_syouhin_syubetu = ("�X�[�p�[","����","�H���i","��","�X�|�[�c�p�i","�d�����i","���e","DVD","�t�@�[�X�g�t�[�h","���p�i","����","�f�U�[�g","�M�t�g","�A���R�[��","��蕨","�Q�[��","�h�����N","�v�v�`","�s�n�v�m");

#���A�̎��
@aisatu_keyword = ("��������","�G�k","�݂�Ȃɒm�点��������","�I�X�X���t�q�k");

#���A���O�̕ۑ�����
$aisatu_max = '50';

#�ő�o�^�Ґ�
$saidai_ninzuu = '250';

#�����t�@�C�������t�H���_�̃p�[�~�b�V�����i777��1�A755��2�j��1�ŃG���[���o��悤�Ȃ�2�������Ă݂Ă��������B
$zidouseisei = "2";

#���b�Z�[�W���̃X�^�C���ݒ�
$message_window ="border: #ff9933; border-style: dotted; border-width: 1px; background-color:#ffffaa; color:336699";

#�X�e�[�^�X���̘g�F
$st_win_wak = "#ff9966";
#�X�e�[�^�X���̔w�i�F
$st_win_back = "#ffffff";

#�ݒu����f���i'�f���̖��O'���u,�v�łȂ����`�Őݒ肵�Ă��������B�����ł̖��O�̓}�E�X���̂������ɃE�C���h�E�ɕ\�������閼�O�ł��B�y�[�W���̃^�C�g����e��f�U�C���E�ݒ�͊Ǘ����j���[�́u�Ǘ��ҍ쐬BBS�̐ݒ�v�ōs���܂��B���ۂɊX�̔C�ӂ̈ʒu�֌f����z�u����̂́A�Ǘ��҃��j���[�́u�X�̃��C�A�E�g�쐬�v�ōs���Ă��������B�j
@admin_bbs_syurui =('�݂�Ȃ̍L��B�����f���ł��B','�^�����BBS�B���i�^��Ɏv���Ă��鎖�𕷂��Ă��܂����B','�I�X�X�����BBS�B���Ȃ��̂��E�ߋ����Ă��������B','�ᔻ�A�v�]�f���@�Ȃɂ������������Ƃ��������炱���ɏ�������ł�������','�V�A�C�e���A�V�E�ƕ�W�f����','��s�W���[���X�J��p�f����','�`�������@�[�g��p�f����','���[�b�N���Z����p�f����','�I�����w�Z���̊F�l�N���ɓ��[�肢�܂��I�x','KITOWN��p�i�{���W������s�j','�v�v�`�l�^�֘A�a�a�r�@�v�v�`�̏o���ҕ�W�A�v�v�`����A���P�[�g�͂�����','�ٔ����@���Ȃ��̈ꌾ�łȂɂ����ς��I','�N�����sICOI�Z���^�[','�����[�b�N�Z���k�b��');

#��L�f���̉摜�i�������ƑΉ�������j
@admin_bbs_gazou =('bbs1.gif','bbs2.gif','bbs3.gif','bbs4.gif','bbs6.gif','bbs5.gif','bbs5.gif','bbs5.gif','bbs8.gif','aisatu.gif','bbs7.gif','chip1061.gif','chip1064.gif','bbs5.gif');

#BBS�̕ۑ��L�����i�e�L���A���X�L�����킹�������ł��j
$bbs_kizi_max = '100';

# �A�N�Z�X���ۂ���z�X�g��
@deny = ("*.host.xx.jp","xxx.xxx.xx.");

#���d�o�^�֎~�i1�ŋ֎~�A0�ŋ֎~���Ȃ��j
$tajuukinsi_flag = '1';

#���d�o�^�҂����O�C���ł��Ȃ�����i1�ł���A0�ł��Ȃ��j
$tajuukinsi_deny = '0';

#�b���[�O�P���̓���
$c_nissuu = '14';

#�b���[�O�̎�����
$c_siaisuu = "100";

#�b���[�O�̎����Ԋu�i�P�ʂ͕��j30koko
$c_siai_kankaku = '1';

#�L�����N�^�[�̉摜�T�C�Y�w��i�w�肵�Ȃ��ꍇ�A���R�T�C�Y�ɂȂ�܂��j
$chara_x_size = '32';	#���T�C�Y
$chara_y_size = '32';	#�c�T�C�Y

#�T�ԊX�R���e�X�g�̏܋��z�i�P�ʂ͖��~�j
$mati_con_syoukin = '3000000';

#�X�R���e�X�g�̓���
$mati_con_nissuu = '7';

#�v���t�B�[���̂P�y�[�W�\����
$hyouzi_max_grobal = '10';

##�ȉ��A�v���t�B�[���ł̑I����
#���ʂ�select
		@sex_array=('','�j','��','����');

#�N���select
		@age_array=('','�`14��','15�`18��','19�`22��','23�`26��','27�`30��','31�`34��','35�`38��','39�`42��','43�`46��','47�`50��','51�΁`');

#�Z����select
		@address_array=('','�k�C��','�X','���','�{��','�H�c','�R�`','����','�Q�n','�Ȗ�','���','���','��t','����','�_�ސ�','�V��','�x�R','�ΐ�','����','�R��','����','��','�É�','���m','�O�d','����','���s','���','����','�ޗ�','�a�̎R','����','����','���R','�L��','�R��','����','����','���Q','���m','����','����','����','�F�{','�啪','�{��','������','����','�C�O');
		
#�I�����v���t�B�[������1
		$prof_name1='�A�s�[���|�C���g';
		@prof_array1=('','����������','��������','�w������','�K�b�V���̊i','�}�b�`��','�D����','��������','�Ԃ�����','��l��炵','�S�ӋC','�f��','�}��','����','�ʔ���','�J���C�C','�L���C','��������','�r������','�i�C�X�o�f�B','�ƒ�I','�X�|�[�c����','�̂����܂�','����������','�G�b�`','�_���l��');

#�I�����v���t�B�[������2
		$prof_name2='��������';
		@prof_array2=('','���l��W��','�F������W��','�����F��W��','��F��W��','���ݗF��W��','���R�����ԕ�W��','�g�o��`��','�s�ϑ����W��','���l��W��','�d����ؒ�','�V����','�ʋ���','�s�ϒ�','�M����','������','������','�Əo��','���}������','�Ўv����');

#�I�����v���t�B�[������3
		$prof_name3='�g��';
		@prof_array3=('','�閧','�Ⴂ','���Ⴂ','����','��⍂��','����');

#�I�����v���t�B�[������4
		$prof_name4='�̏d';
		@prof_array4=('','�閧','�₹�Ă�','�����₹�Ă�','����','���ۂ���','�ۂ���');

#�I�����v���t�B�[������5
		$prof_name5='�E��';
		@prof_array5=('','�t���[�^�[','�w��','���E','�n�k','�T�����[�}��','������','��w','�c�ƃ}��','�Z�p�E','���Ѓ}��','��s�}��','SE�E�v���O���}�[','�p�C���b�g','�X�`�����[�f�X','�x�@','���h�m','�m��','�t�@�b�V�����֌W','�v�����i�[','�ҏW��','�N���G�C�^�[','�̔���','���e�t','��H','�}�X�R�~','�В�','��Ж���','�����E','�R���s���[�^','���H��','���t','��t','�A�[�e�B�X�g','�f�U�C�i�[','�^�����g','�Ō�w','�ە�','�R���T���^���g','���c��','������','���y�֌W','�|�l','�X�|�[�c�I��','���̑�');
		
#�L�q���v���t�B�[������
	@kijutu_prof = ('���Ă���L���l','�','�z�[���y�[�W','��_','�D���ȗL���l','�D���ȃX�|�[�c','�D���ȉf��','�D���Ȃs�u�ԑg','�D���ȉ��y','�D���Ȉِ��̃^�C�v','�����̖�','�����Ȃ���','����ԍs�������Ƃ���','����Ԃ���������','�ꌾ�R�����g');

##�ȉ��e��f�U�C���̃X�^�C���ݒ�
#���b�Z�[�W���̃X�^�C���ݒ�
$message_win ="border: #0000ff; border-style: dotted; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; background-color:#ffffff; color:000000";

$town_stylesheet =<< "EOM";
.dai {  font-size: 13px; font-weight: bold;color: #000000}	/*�傫�ȕ���*/
.tyuu {  font-size: 13px; color: #ff6600}	/*�X�e�[�^�X�����o��*/
.honbun2 {  font-size: 13px; line-height: 16px; color: #006699}	/*�X�e�[�^�X���ڕ���*/
.honbun3 {  font-size: 13px; line-height: 13px; color: #006699}	/*�p�����[�^���ڕ���*/
.honbun5 {  font-size: 13px; line-height: 13px; color: #339900}	/*�L�����̃p�����[�^���ڕ���*/
.honbun4 {  font-size: 13px; line-height: 22px; color: #006699}	/*�����炢�̕���*/
.job_messe {  font-size: 13px; line-height: 22px; color: #000000}	/*�p�����[�^���b�Z�[�W*/
.small {  font-size: 13px; color: #444444}	/*����������*/
.midasi {  font-size: 16px; font-weight: bold; text-align: center;color: #666666}	/*�X�̖��O*/
.gym_style { background-color:#ffcc33; background-image:url($img_dir/shop_bak.gif)}	/*�W���̔w�i*/
.syokudou_style { background-color:#ccff66; background-image:url($img_dir/shop_bak.gif)}	/*�H���̔w�i*/
.orosi_style { background-color:#996633; background-image:url($img_dir/shop_bak.gif)}	/*���≮�̔w�i*/
.job_style { background-color:#669966; background-image:url($img_dir/shop_bak.gif)}	/*�n���[���[�N�̔w�i*/
.school_style { background-color:#339999; background-image:url($img_dir/shop_bak.gif)}	/*�w�Z�̔w�i*/
.ginkou_style { background-color:#999999; background-image:url($img_dir/shop_bak.gif)}	/*��s�̔w�i*/
.yakuba_style { background-color:#336699; background-image:url($img_dir/shop_bak.gif)}	/*����̔w�i*/
.item_style { background-color:#ffcc66; background-image:url($img_dir/command_bak.gif)}	/*�A�C�e���g�p��ʂ̔w�i*/
.kentiku_style { background-color:#996666; background-image:url($img_dir/command_bak.gif)}	/*���z��Ђ̔w�i*/
.omise_list_style { background-color:#b293ad; background-image:url($img_dir/shop_bak.gif)}	/*�l���X�̏��i���X�g�w�i*/
.prof_style { background-color:#ccff99; background-image:url($img_dir/shop_bak.gif)}	/*�v���t�B�[����ʔw�i*/
.keiba_style { background-color:#99cc66; }	/*���n�w�i*/

.yosumi {  border: #666666; border-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; background-color:#ffffff}	/*�X�X�e�[�^�X��*/

.sumi {  border: #000000; border-style: solid; border-top-width: 0px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 0px}
.migi {  border: #000000; border-style: solid; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px}
.sita {  border: #000000; border-style: solid; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px}
.sita2 {  border: #666666; border-style: solid; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px}
.jouge {  border: #000000; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px}
.message {  font-size: 13px; line-height: 16px; color: #000000;}


.purasu {color: #009900;}
.mainasu { color: #ff3300;}
.kuro {  font-size: 13px; text-align: left;color: #000000}
.honbun {  font-size: 13px; line-height: 16px; color: #000000}
.loto {  font-size: 28px; color: #000000;line-height:180%;}
.naka {  border: #000000; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px}
a {color:#333333;text-decoration: none}
a:hover {text-decoration: underline}
body {font-size:13px;color:#000000 }
table {font-size:13px;color:#000000;}
EOM

##########################ver.1.1�ǉ�
#�M�t�g���L���x���i����ꂽ�M�t�g�j
$gift_gendo = '10';

#�M�t�g�w�����x��
$kounyu_gift_gendo = '10';

#�����̂��X�ɒu���鏤�i�A�C�e����
$mise_zaiko_gendo = '100';

#�A�C�e���������x�ȏ�Ȃ瓯���A�C�e���ł��݌ɂ𑝂₹�Ȃ�����i���₹�Ȃ���1�A���₹�遁0�j
$douitem_ok = '0';

#����������ɒʏ�̉��{�̑����Ńp���[���񕜂��邩
$onsen_times = '10';

#����Ŏg���Ă���摜�̐��i����̉摜��ǉ�����ꍇ�Aimg/onsen�t�H���_�[���Ɂ�.jpg�i����1����n�܂�A�Ԃ̐����j�Ƃ����t�@�C�����œ���Ă��������j
$on_gazou_suu = '10';

#����������i�P�ʂ͉~�j
$nyuuyokuryou = '100';

#gzip�̃p�X�i�T�[�o�[��gzip���k�ɑΉ����Ă��Ȃ��ꍇ�󗓂ɂ��Ă��������i����ʂ��^�����ɂȂ�ꍇ�Ȃǂ͑Ή����ĂȂ��\���������ł��j�B�������Agzip���k���g����ƃe�L�X�g�̓]���ʂ����Ȃ菬�����ł��܂��j
$gzip = '';

#�k���ŊX�̈ړ��ɂ����鎞�ԁi�b�w��j
$matiidou_time = '30';

#�e��蕨���Ƃňړ��ɂ����鎞�ԁi'��蕨','������b��'�̃t�H�[�}�b�g�ŁB��蕨��syouhin.dat�ɂ��鏤�i�łȂ��ƈӖ�������܂���B���������i��ʂ��u��蕨�v�ł���K�v�͂���܂���B�R�����g�Ɂu���ړ���i�ł��v�Ɠ���Ă����������e�؂��Ǝv���܂��B�܂��������̂����ɕ��ׂĂ��������j
%idou_syudan =('���]��','15','���P�b�g','5','�����]�����u','0','������','20','�����j���O�V���[�Y','17','���[���[�X���[�S�[�S�[','�x�X�p','10','�X�[�p�[�J�u','10','�h�D�J�e�B','7','�i�i�n��','7','�J���[��','7','�{���{','6','�L���f���b�N','6','�x���c','5','���[���X���C�X','5','�X�J�C���C��GTR','4','���[�^�X���[���b�p','4','�A���t�@�����I','4','�W���K�[','4','BMW','4','�t�F�A���f�BZ','5','15','�|���V�F','3','�t�F���[��','2','�~�O25','3');

#�X�ړ����Ɏ��̂��N�����m���i�����̈�̊m�����Ŏw��B�f�t�H���g�ł�10���̂P�Ƃ����Ӗ��j
$ziko_kakuritu = '20';

#�s���������ԁi�b�w��B������t���Ȃ��ꍇ��0�j
$koudou_seigen = '5';

#�J�[�h�Q�[�����ł���Ԋu�i�P�ʁF���j
$crad_game_time = '1';

##########################ver.1.2�ǉ�

#����A�C�e���̏��L���̌��x
$item_kosuuseigen = '5';

#�d�����ł���Ԋu�i�P�ʁF���B���������̏ꍇ��0���w��j
$work_seigen_time = '1';

#���n�̍w�����x�����i�P�ʁF���j
$keiba_gendomaisuu = '1000000';

##########################ver.1.21�ǉ�
#�����o�[���O�̃t�@�C�����b�N�����i0�Ń��l�[�����b�N�A0�ł��܂��ғ����Ȃ��ꍇ1�ɂ��Ă��������j
$mem_lock_num = '0';


##########################ver.1.3�ǉ�
#���l�����v���t�B�[���L�^�t�@�C��
$as_profile_file='./log_dir/as_pfofilelog.cgi';
#�J�b�v���L�^�t�@�C��
$couple_file='./log_dir/couplelog.cgi';
#�q���L�^�t�@�C��
$kodomo_file='./log_dir/kodomolog.cgi';
#�X�j���[�X�L�^�t�@�C��
$news_file='./log_dir/mati_news.cgi';

#����̃j���[�X�\������
$news_kensuu = '100';

#���X�ɒu���Ă�����݌ɂ̏����
$mise_zaiko_limit = '100';

#���[���̕ۑ�����
$mail_hozon_gandosuu = '50';

#���ʕ��C�͉��{�̑��x�ŉ񕜂��邩
$tokubetu_times = '100000000';

#���ʕ��C�ł������p�i�~�j
$tokubetuburo_hiyou = '1000000';

#koko2006/03/31
#�����C�͉��{�̑��x�ŉ񕜂��邩
$matu_times = '100';
#�����C�ł������p�i�~�j
$matu_hiyou = '5000';
#�|���C�͉��{�̑��x�ŉ񕜂��邩
$take_times = '200';
#�|���C�ł������p�i�~�j
$take_hiyou = '20000';
#�~���C�ł������p�i�~�j
$ume_times = '500';
#�~���C�ł������p�i�~�j
$ume_hiyou = '100000';
#kokoend2006/03/31

#�����V�X�e�����g�����i1���g���A0���g��Ȃ��@��0�ɂ��邱�ƂŃn�[�g���q���A�C�R�����o������Ȃ��Ȃ�܂��B�܂��A0�̏ꍇ�u���l�������v���X�ɐݒu���Ȃ��ł��������j
$renai_system_on = '1';

#�����ɕK�v��LOVE�p�����[�^�̐��l
$need_love = '200';

#�����̗�����������i�����Ȃ���0�A�����遁1�j
$douseiai_per = '0';

#�����ɉ��l�Ƃ������邩�i�z��ҁ{���l�j
$koibito_seigen = '5';

#�����ɕK�v�ȃ��u���u�x�i�v���o���l�̍��v�j
$aijou_kijun = '500';

#�����ɕK�v�Ȏv���o���l�i���ꂼ��̎v���o�̍Œ�l�j
$omoide_kijun = '80';

#���l�Ɖ����ԃf�[�g�����Ȃ��ƕʂ�Ă��܂���
$wakare_limit_koibito = '7';

#�z��҂Ɖ����ԃf�[�g�����Ȃ��ƕʂ�Ă��܂���
$wakare_limit_haiguu = '9';

#���肪�z��҂̏ꍇ�̎q�����ł���m���i10�Ȃ�10���̂P�̊m���jkoko
$kodomo_kakuritu1 = '7';

#���肪���l�̏ꍇ�̎q�����ł���m���i80�Ȃ�80���̂P�̊m���jkoko
$kodomo_kakuritu2 = '15';

#�q��Ăł���Ԋu�i�P�ʁF���ԁj
$kosodate_kankaku = '3';

#�q���̃p�����[�^���P������̂ɂ������p�i�~�j
$youikuhiyou = '20000';

#�����Ԏq���ɐH����^���Ȃ��Ǝ���ł��܂���
$kodomo_sibou_time = '7';

#�q���͉��΂܂Ő����邩�i�d���肪�����Ă�����ԁj
$kodomo_sibou_time2 = '70';

#�ȉ��A�����������ł̕ύX�\�ȃv���t�B�[������
#�N���select
		@as_age_array=('','�`14��','15�`18��','19�`22��','23�`26��','27�`30��','31�`34��','35�`38��','39�`42��','43�`46��','47�`50��','51�΁`');

#�Z����select
		@as_address_array=('','�k�C��','�X','���','�{��','�H�c','�R�`','����','�Q�n','�Ȗ�','���','���','��t','����','�_�ސ�','�V��','�x�R','�ΐ�','����','�R��','����','��','�É�','���m','�O�d','����','���s','���','����','�ޗ�','�a�̎R','����','����','���R','�L��','�R��','����','����','���Q','���m','����','����','����','�F�{','�啪','�{��','������','����','�C�O');

#�I�����v���t�B�[������1
		$as_prof_name2='�A�s�[���|�C���g';
		@as_prof_array2=('','����������','��������','�w������','�K�b�V���̊i','�}�b�`��','�D����','��������','�Ԃ�����','��l��炵','�S�ӋC','�f��','�}��','����','�ʔ���','�J���C�C','�L���C','��������','�r������','�i�C�X�o�f�B','�ƒ�I','�X�|�[�c����','�̂����܂�','����������','�G�b�`','�_���l��');

#�I�����v���t�B�[������2
		$as_prof_name3='�Z��ł���X';
		@as_prof_array3=('','�Ƃ������Ă��Ȃ�','���C���X�g���[�g','�V�[���]�[�g','�J���g���[�^�E��','�_�E���^�E��');

#�I�����v���t�B�[������3
		$as_prof_name4='�~�����q���̐�';
		@as_prof_array4=('','�q���͂���Ȃ�','1�l�ł���','2�l���炢','3�l���炢','4�A5�l�͗~����','6�l�ȏ�');

#�I�����v���t�B�[������4
		$as_prof_name5='����̔N���';
		@as_prof_array5=('','�N��͋C�ɂ��Ȃ�','�������炢������','�N�オ����','�N��������','�������N�オ����','�������N��������');

#�I�����v���t�B�[������5
		$as_prof_name6='����ɖ]�ނ���';
		@as_prof_array6=('','�������悳','���̂悳','�w�̍���','�K�b�V���̊i','�}�b�`��','�D����','�T���x','��l��炵','�S�ӋC','�f����','�}����','������','�ʔ���','�J���C��','�L���C��','���̑傫��','�r�̃L���C��','�i�C�X�o�f�B','�ƒ�I','�X�|�[�c�}��','�̂̂��܂�','�����̏�肳','�G�b�`��');

#�X�̉��Ɉ��A��\�����邩�i�\�����遁1�A�\�����Ȃ���0�j
$top_aisatu_hyouzi = '1'; #koko

#��ŕ\������ɂ����ꍇ�̕\������
$top_aisatu_hyouzikensuu = '20';
#��ŕ\������ɂ����ꍇ�̖��O�̐F
$top_aisatu_hyouzi_iro1 = '#333399';
#��ŕ\������ɂ����ꍇ�̋L���̐F
$top_aisatu_hyouzi_iro2 = '#333333';

#�g�b�v�y�[�W�ŊX�̉��Ɏ��R�\�����邷��html�iEOM�`EOM�̊Ԃ�html�ŋL�q�j
$top_information =<< "EOM";
<div align="center"><br><br>
<iframe src="./coun0/counter0.cgi" name="counter" width="170" height="40" scrolling="no">�J�E���^�[</iframe>
<br>
</div>
<Table Border>
<Tr>
<Td>
�����s�n�v�m<br>
<a href="http://w3.oroti.com/~wgs/cgi-bin/EBNC/town_maker.cgi"><img src="ebnctop.gif"></a><br>
<a href="http://oroti.com/~poke/town_hairu/"><img src="new_poketown.gif"></a><br>
</Td>
</Tr>
</Table> 
EOM

##########################ver.1.30�ǉ�
# �Q���҂�\������i1���\���A0���\�����Ȃ��j
$sanka_hyouzi_kinou = '1';

# ��Łu�\���v�ɂ����ꍇ�̕\���ʒu�i1����A0�����j
$sanka_hyouzi_iti = '1';

#�����Ƀ��O�C���ł���l��
$douzi_login_ninzuu = 20;

##########################ver.1.40�ǉ�
# �Q���҃t�@�C���iver.1.30��"./log_dir/guestlog.cgi"�������w���ύX�j
$guestfile = "./guestlog_00.cgi";

#�Q�[�����Ȃ��Ń��O�A�E�g����܂ł̎��ԁi�b�j
$logout_time = '1200';

#�V�K�o�^�̎󂯕t���i1���������Ȃ��A0����������jkoko
$new_touroku_per = '0';

#���O���p�X���[�h�L�^�t�@�C��
$pass_logfile = './log_dir/passlog.cgi';

#������z��҂̂��X�ŏ��i�𔃂��Ȃ�����i1�������Ȃ��A0��������j
$kaenai_seigen = '0';

############## �ǉ� ###################
# �����������i������i�ڂ������Ă��Ȃ��Ɣ����Ȃ��������
$kyokasuru = '';#'�R�[�q�[';
$kyokahin2 = '';#'�o�C�A�O��';
# �����i�ڃ��X�g��L���i�������Ă��Ȃ��Ƃ��̏��i�͔����Ȃ��Ȃ�B
@kyokahitsuyou = ('�r�b�O�}�b�N','���|�r�^��D','���R���X','�R�[�q�[','�o�C�A�O��','�t�F����������','Apple1','�u���^�������o�[�Y�J�[�h');

#######################################

#------------------�ݒ�ύX�����܂Łi�ȉ��͕K�v������ΕύX���Ă��������j
#�X�N���v�g�̖��O
$script='./town_maker.cgi';
#�l���O�f�[�^�t�@�C��
$logfile='./log_dir/memberlog.cgi';
#�b���[�O���O�f�[�^�t�@�C��
$doukyo_logfile='./log_dir/doukyo_log.cgi';
#�I���W�i���ƃ��X�g�t�@�C��
$ori_ie_list='./log_dir/ori_ie_log.cgi';
#���C���X�p�����[�^�L�^�t�@�C��
$maintown_logfile='./log_dir/maintownlog.cgi';
#�����i�L�^�t�@�C��
$orosi_logfile='./log_dir/orosilog.cgi';
#�����̐H�����j���[�L�^�t�@�C��
$syokudou_logfile='./log_dir/syokudoulog.cgi';
#�����̃f�p�[�g�̕i�����L�^�t�@�C��
$depart_logfile='./log_dir/departlog.cgi';
#���A���O�L�^�t�@�C��
$aisatu_logfile='./log_dir/aisatulog.cgi';
#�X�R���e�X�g���O�t�@�C��
$maticon_logfile='./log_dir/maticonlog.cgi';
#�X�R���e�X�g���J�҃��O�t�@�C��
$kourousya_logfile='./log_dir/kourousyalog.cgi';
#�h�[�i�c�Q�[�����O�t�@�C��
$donuts_logfile='./log_dir/donutslog.cgi';
#�h�[�i�c�Q�[�����O�t�@�C��2#koko
#$donuts2_logfile='./log_dir/donutslog2.cgi';
#���n���O�t�@�C��
$keiba_logfile='./log_dir/keibalog.cgi';
#���n�����L���O���O�t�@�C��
$keibarank_logfile='./log_dir/keibaranklog.cgi';
#���b�N�t�@�C����
$lockfile = './lock';
#���n���b�N�t�@�C����
$keibalockfile = './lock2';
#�v���t�B�[���L�^�t�@�C��
$profile_file='./log_dir/pfofilelog.cgi';

1;
