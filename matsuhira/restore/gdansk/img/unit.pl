#
# eval{ flock (OI, 2); }; 2007/06/16
#
sub get_unit {
##################�p�[�c���̒�`�i�����Œ�`���ꂽ�p�[�c�͊Ǘ��҃��j���[�́u�X�̃��C�A�E�g�쐬�v�Ɍ���܂��B
	%unit = (
#�摜�݂̂̃p�[�c�i�����̍D���ȃp�[�c�摜�𑝂₵�����ꍇ�́A���̃t�H�[�}�b�g���Q�l�ɒǉ����Ă��������B�摜�f�[�^��img�t�H���_�ɓ���Ă��������B�摜�͑S��32px �~ 32px�ɓ��ꂷ��K�v������܂��B�p�[�c��`�͂��̂܂܂ŉ摜�f�[�^�݂̂𓯂��t�@�C�����̔C�ӂ̉摜�ɍ����ւ��Ă�OK�ł��j
#�@"�L��" => "<td><img src=$img_dir/�摜�t�@�C����></td>",
#�@���u�L���v�͎��ʂ��₷���C�ӂ̕��������č\���܂��񂪁A���܂蒷���Ȃ�Ȃ��悤�ɂ��܂��傤�i�ł��邾���Q�����ȓ��j�B�܂����ƃ_�u��Ȃ��悤�ɒ��ӂ��Ă��������B

#ver.1.30	�p�[�c��html�L�q���������ȗ���
"����" => "<td><img src=$img_dir/kousa_r.gif></td>",
"����" => "<td><img src=$img_dir/yoko_r.gif></td>",
"���c" => "<td><img src=$img_dir/tate_r.gif></td>",
"��" => "<td><img src=$img_dir/chip1037.gif></td>",
"�C��" => "<td><img src=$img_dir/rikyo.gif></td>",
"��1" => "<td><img src=$img_dir/tree1.gif></td>",
"��2" => "<td><img src=$img_dir/tree2.gif></td>",
"��3" => "<td><img src=$img_dir/tree3.gif></td>",
"��4" => "<td><img src=$img_dir/tree4.gif></td>",
"�C" => "<td><img src=$img_dir/asase.gif></td>",
"��" => "<td><img src=$img_dir/chip10.gif></td>",
"�F��" => "<td><img src=$img_dir/utyu.gif></td>",
"�C��" => "<td><img src=$img_dir/ui.gif></td>",
"�R��" => "<td><img src=$img_dir/chipt002.gif></td>",
"�~�T" => "<td><img src=$img_dir/land9.gif></td>",
"��" => "<td><img src=$img_dir/land2.gif></td>",
"�X" => "<td><img src=$img_dir/land6.gif></td>",
"��" => "<td><img src=$img_dir/land690.gif></td>",
"���X" => "<td><img src=$img_dir/chip1028.gif></td>",
"���X" => "<td><img src=$img_dir/land1.gif></td>",
"���" => "<td><img src=$img_dir/land60.gif></td>",
"��_" => "<td><img src=$img_dir/monument0.gif></td>",
"�w1" => "<td><img src=$img_dir/house21.gif></td>",
"�w2" => "<td><img src=$img_dir/land8.gif></td>",
"�H1" => "<td><img src=$img_dir/Senro5.png></td>",
"�H2" => "<td><img src=$img_dir/Senro3.png></td>",
"�H3" => "<td><img src=$img_dir/Senro2.png></td>",
"�H4" => "<td><img src=$img_dir/Senro4.png></td>",
"�H5" => "<td><img src=$img_dir/Senro1.png></td>",
"�H6" => "<td><img src=$img_dir/Senro6.png></td>",
"��1" => "<td><img src=$img_dir/chip10025.gif></td>",
"��2" => "<td><img src=$img_dir/chip10024.gif></td>",
"��3" => "<td><img src=$img_dir/house102.gif></td>",
"��4" => "<td><img src=$img_dir/house100.gif></td>",
"����" => "<td><img src=$img_dir/rail_l.png></td>",
"���E" => "<td><img src=$img_dir/rail_r.png></td>",

#�����N�p�p�[�c�i�o���s�s�ȂǊX���瑼��URL�փ����N��\��ꍇ�̃t�H�[�}�b�g�ł��B�V���ɒǉ�����ꍇ�́A���̃t�H�[�}�b�g���R�s�[���Ă���A�L���AURL�A�����A�K�v�Ȃ�Ή摜�t�@�C������ύX���Ă��������j
#�@"�L��" => "<td><a href=\"�����N���URL\" target=_blank><img src='$img_dir/�摜��'  width=32 height=32 border=0  onMouseOver='onMes5(\"�}�E�X���̂����Ƃ��\����������\")' onMouseOut='onMes5(\"\")'></a></td>",
#�@���͏������̃T���v���ł��B���ۂɂ�����X�ɐݒu���Ȃ��ł��������B

"�����N" => "<td><a href=\"http://brassiere.jp/03com/town2/town_maker.cgi\" target=_blank><img src='$img_dir/link.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�e�X�g�Q���p�̃T���v���ݒu�v���O�����ł��B\")' onMouseOut='onMes5(\"\")'></a></td>\n",

"����" => "<td><a href=\"./setumei.htm\" target=_blank><img src='$img_dir/link.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"���S�҂ւ̐����B\")' onMouseOut='onMes5(\"\")' alt='���S�҂ւ̐����B'></a></td>\n",

"�A��" => "<td><a href=\"./bbs0/bbs0.cgi\" target=_blank><img src='$img_dir/renraku.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�����Ȃ��Ȃ������̘A���p�ł��B\")' onMouseOut='onMes5(\"\")'></a></td>\n",

#�@�\���������p�[�c�i�ȉ��́A���ꂼ��@�\�������������Ȃǂւ̃����N�ɂȂ�܂��̂ŁA��{�I�ɕύX�͂��Ȃ��ł��������B�K�v�ł���΁A�����A�摜�t�@�C�����isrc='$img_dir/����.gif�̕����j�̕ύX�͉j

"�A�C�e��" => "<form method=POST action=\"item.cgi\"><input type=hidden name=mode value=\"item_make\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/img062.gif'  onMouseOver='onMes5(\"�A�C�e���̃A�C�f�A�Љ�E�o�^�B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#koko2005/12/03

"����" => "<form method=POST action=\"yakuba.cgi\"><td height=32 width=32><input type=hidden name=mode value=yakuba><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/chip1064.gif'  onMouseOver='onMes5(\"��s���ł��B�V�K�ɏZ���o�^���ꂽ���⃉���L���O�����邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"��s" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=\"ginkou\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/bank.gif'  onMouseOver='onMes5(\"��s�ł��B������a����������o������ł��܂��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�a�@" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=byouin><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><td height=32 width=32><input type=image src='$img_dir/hospi.gif'  onMouseOver='onMes5(\"�a�@�ł��B��p�͍��߂ł����A�قƂ�ǂ̕a�C��S�������܂��B\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"�J�[�h" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=\"donus\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"�O�̐l���������J�[�h�Ɠ����������o���Ȃ��悤�ɂ���J�[�h�Q�[���ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40
"�J�[�h�Q" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=\"donus2\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"�O�̐l���������J�[�h�Ɠ����������o���Ȃ��悤�ɂ���J�[�h�Q�[���Q�ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�J�[�h�R" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=\"donus3\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"�O�̐l���������J�[�h�Ɠ����������o���悤�ɂ���J�[�h�Q�[���R�ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�J�[�h�S" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=\"donus4\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"High��Low�𓖂Ă�Q�[���ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�X���b�g" => "<form method=POST action=\"slot.cgi\"><input type=hidden name=mode value=\"l1_slot\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"�X���b�g�ŗV�ڂ��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�T�C�R��" => "<form method=POST action=\"saikoro.cgi\"><input type=hidden name=mode value=\"saikoro\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"�T�C�R���ŗV�ڂ��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"����" => "<form method=POST action=\"otakara.cgi\"><input type=hidden name=mode value=\"otakara\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/takara.gif'  onMouseOver='onMes5(\"����Q�[��\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�M�t�g��" => "<form method=POST action=\"gifutoya.cgi\"><input type=hidden name=mode value=gifutoya><input type=hidden name=mysec value=$in{'mysec'}><!-- koko2006/04/01 --><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><td height=32 width=32><input type=image src='$img_dir/gft.gif'  onMouseOver='onMes5(\"�M�t�g�쐬��\")' onMouseOut='onMes5(\"\")'></td></form>",

"�}���`" => "<form method=POST action=\"cardw2.cgi\"><input type=hidden name=mode value=\"cardw\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"�}���`�J�[�h����B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"����" => "<form method=POST action=\"kuzi.cgi\"><input type=hidden name=mode value=\"kuzi_game\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/kuji.gif'  onMouseOver='onMes5(\"��������B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"���g" => "<form method=POST action=\"loto.cgi\"><input type=hidden name=mode value=\"loto_game\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"���g����B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"���g6" => "<form method=POST action=\"loto6.cgi\"><input type=hidden name=mode value=\"loto_game\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"���g6����B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"��" => "<form method=POST action=\"kabu.cgi\"><input type=hidden name=mode value=\"kabu\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/kabu.gif'  onMouseOver='onMes5(\"���̎����\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�H��" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"syokudou\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/syokudou.gif'  onMouseOver='onMes5(\"�Z���g�����H���ł��B��ނ͖L�x�ł����A�l�i�͍��߂ō݌ɂ����Ȃ߂ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",
#koko2006/07/16
"�H���Q" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"syokudou2\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/syokudou.gif'  onMouseOver='onMes5(\"�Z���g�����H���Q�ł��B��ނ͖L�x�ł����A�l�i�͍��߂ō݌ɂ����Ȃ߂ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�f�p" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"depart_gamen\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/depart.gif'  onMouseOver='onMes5(\"�����f�p�[�g�ł��B��ނ͖L�x�ł����A�l�i�͍��߂ō݌ɂ����Ȃ߂ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�f�p2" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"depart_gamen2\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/depart.gif'  onMouseOver='onMes5(\"���C�o���f�p�[�g�ł��B��ނ͖L�x�ł����A�l�i�͍��߂ō݌ɂ����Ȃ߂ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"���̋@" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"hanbai\"><input type=hidden name=mysec value=\"$in{'mysec'}\"><!-- koko2006/04/01 --><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/zidou2.gif'  onMouseOver='onMes5(\"�����̔��@�ł��B\")' onMouseOut='onMes5(\"\")'></td></form>",

"�̔�1" => "<form method=POST action=\"hanbai1.cgi\"><input type=hidden name=mode value=\"hanbai1\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/house1.gif'  onMouseOver='onMes5(\"���X1\")' onMouseOut='onMes5(\"\")'></td></form>",

"���T�C" => "<form method=POST action=\"recycle.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"resycle\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/resai.gif'  onMouseOver='onMes5(\"���T�C�N���V���b�v�ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�N�[�|��" => "<form method=POST action=\"coupon.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"coupon\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/reload.gif'  onMouseOver='onMes5(\"�N�[�|���������ł��B\")' onMouseOut='onMes5(\"\")'></td></form>",

"����" => "<form method=POST action=\"fukubiki.cgi\"><input type=hidden name=mode value=\"fukubiki\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/fukubiki.gif'  onMouseOver='onMes5(\"�����Q�[��\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�W��" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"gym\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/gym.gif'  onMouseOver='onMes5(\"�X�|�[�c�W���ł��B�̂�b���邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�w�Z" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"school\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/school.gif'    onMouseOver='onMes5(\"�X�N�[���ł��B����̔\\�͂�L�΂��̂ɑ傫�Ȍ��ʂ�����܂����A1��1���b�X���ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",
#koko 2005/09/11
"����" => "<form method=POST action=\"kyushitu.cgi\"><td height=32 width=32><input type=hidden name=mode value=kyushitu><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/house21.gif'  onMouseOver='onMes5(\"�}���`�J���`���[�X�N�[���ł��A�Ȃ�ł��b�����܂�\")' onMouseOut='onMes5(\"\")'></td></form>",
#kokoend
"�E��" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"job_change\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/work.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�E�ƈ��菊�ł��B�A�E�A�]�E�Ȃǂ͂�����ցB\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"��n" => "<td><img src=$img_dir/akiti.gif onMouseOver='onMes5(\"���̏ꏊ�ɉƂ����Ă邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td>\n",
"��n2" => "<td><img src=$img_dir/battle.gif onMouseOver='onMes5(\"���̏ꏊ�ɉƂ����Ă邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td>\n",
#koko2007/03/29
"��n3" => "<td><img src=$img_dir/akiti3.gif onMouseOver='onMes5(\"���̏ꏊ�ɉƂ����Ă邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td>\n",
"��n4" => "<td><img src=$img_dir/akiti3.gif onMouseOver='onMes5(\"���̏ꏊ�ɉƂ����Ă邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td>\n",
#koko2007/05/02
"�≮" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"orosi\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/tonya.gif\" onMouseOver='onMes5(\"���X���Ƃ������Ă���l�́A�����ŏ��i���d����邱�Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"���z" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=\"kentiku\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/kentiku.gif\"  onMouseOver='onMes5(\"���݉�Ђł��B�Ƃ����Ă����Ƃ��͂����Ɉ˗����܂��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"���n" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"keiba\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/keiba.gif\"  onMouseOver='onMes5(\"���n��ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",			#ver.1.40

"�v���t" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"prof\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/prof.gif\"  onMouseOver='onMes5(\"�Z���̎��ۂ̃v���t�B�[����o�^����Ƃ���ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�L����" => "<form method=POST action=\"game.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"c_league\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/chara_battle.gif\"  onMouseOver='onMes5(\"�ŋ��̃L�����N�^�[�����߂�wC���[�O�x���ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�X�R��" => "<form method=POST action=\"./mati_contest.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"matikon\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/matikon.gif\"  onMouseOver='onMes5(\"�X�̖��_�������ċ����w�T�ԊX�R���e�X�g�x�ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40

"�n" => "<td><img src=$img_dir/kentiku_yotei.gif width=32 height=32  width=32 height=32 border=0 onMouseOver='onMes5(\"���z�\\��n�ł��B\")' onMouseOut='onMes5(\"\")'></td>\n",

#�o�[�W�����A�b�v���ɂ��V�����@�\�p�[�c���ʂɒǉ�����ꍇ�A�u��������v�`�u�����܂Łv�̊Ԃɒǉ����Ă��������B
####�u��������v
"��" => "<td><img src=$img_dir/sora.gif></td>",
"��" => "<td><img src=$img_dir/kabe.gif></td>",
"24" => "<td><a href=\"http://hirarira.hp.infoseek.co.jp/24LIFE/24LIFE.html\" target=_blank><img src='$img_dir/24LIFE.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"24LIFE�Ɉړ����܂�\")' onMouseOut='onMes5(\"\")'></a></td>",
"�Q��" => "<td><a href=\"http://hirarira.hp.infoseek.co.jp/newwwa/newwwa.html\" target=_blank><img src='$img_dir/game.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�V�v�v�`�Q�[���Z���^�[�ł�\")' onMouseOut='onMes5(\"\")'></a></td>",
"�g" => "<td><a href=\"http://w1.oroti.com/~wgsv2/town/town_maker.cgi\" target=_blank><img src='$img_dir/yoko_r.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�d�]�_�s�ɔ�т܂�\")' onMouseOut='onMes5(\"\")'></a></td>",
"�u" => "<td><a href=\"http://aaaa2000.hp.infoseek.co.jp/cgi-bin/townof2nd/town_maker.cgi\" target=_blank><img src='$img_dir/yoko_r.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�u�����B�u�^�E���ɔ�т܂�\")' onMouseOut='onMes5(\"\")'></a></td>",
"����" => "<td><img src='$img_dir/chip1065.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�����ł�\")' onMouseOut='onMes5(\"\")'></a></td>",
"�`" => "<td><img src='$img_dir/chip1045.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�`�ł�\")' onMouseOut='onMes5(\"\")'></a></td>",
"���̂�" => "<td><img src='$img_dir/monster0.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"���̂�ł�\")' onMouseOut='onMes5(\"\")'></a></td>",
"��1" => "<td><img src='$img_dir/JJ1.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�����[��\")' onMouseOut='onMes5(\"\")'></a></td>",
"��2" => "<td><img src='$img_dir/JJ2.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�₠�₠�B�ɍ׃|�b�L�[�͂��邩���H\")' onMouseOut='onMes5(\"\")'></a></td>",
"��3" => "<td><img src='$img_dir/JJ3.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"���[�H\")' onMouseOut='onMes5(\"\")'></a></td>",
"��4" => "<td><img src='$img_dir/JJ4.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�����[��E�E�E�B\")' onMouseOut='onMes5(\"\")'></a></td>",
"��5" => "<td><img src='$img_dir/JJ5.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�킟��\")' onMouseOut='onMes5(\"\")'></a></td>",
"��6" => "<td><img src='$img_dir/JJ6.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�{�̂̉J�{���J����낵����\")' onMouseOut='onMes5(\"\")'></a></td>",
"��7" => "<td><img src='$img_dir/JJ7.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�����[��H\")' onMouseOut='onMes5(\"\")'></a></td>",
"��8" => "<td><img src='$img_dir/JJ8.png'  width=32 height=32 border=0  onMouseOver='onMes5(\"�ӂ��E�E�E�B\")' onMouseOut='onMes5(\"\")'></a></td>",
"�w1" => "<td><img src='$img_dir/station.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"�w�ł��A���ݓd�Ԃɂ͏��܂���\")' onMouseOut='onMes5(\"\")'></a></td>",
"��" => "<td><img src='$img_dir/monument1.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"���q�������[���O���̋L�O��ł�\")' onMouseOut='onMes5(\"\")'></a></td>",
#ver.1.1�ǉ�
"����" => "<!-- koko2006/04/10-->
<script type=\"text/javascript\">
<!--
function on_sec(){
	myonDate = Math.round((new Date()).getTime()/1000);
	document.onsen.onsec.value = myonDate;
}
//-->
</script>
<!-- kokoend -->
<form method=POST name=onsen action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"onsen\"><input type=hidden name=onsec value=\"\"><!-- koko 2007/06/11 --><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/onsen_a.gif\"  onMouseOver='onMes5(\"����ł��B��ꂽ�̂�����܂��傤�B��������$nyuuyokuryou�~�ł��B\")' onMouseOut='onMes5(\"\")' onClick=\"on_sec()\"></td></form>\n",	#ver.1.40

#ver.1.3�ǉ�
"����" => "<form method=POST action=\"kekkon.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"assenjo\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/assenjo.gif\"  onMouseOver='onMes5(\"���l�������ł��B�o�[�`�����ȗ����⌋�������������͂�����֓o�^���Ă��������B\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40
####
"�X1_1" => "<form method=POST action=\"$script\"><input type=hidden name=mode value=\"login_view\"><input type=hidden name=command value=\"mati_idou\"><td height=32 width=32><input type=hidden name=maemati value=\"$in{'town_no'}\"><input type=hidden name=town_no value=\"0\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=image src=\"$img_dir/my_housein.gif\"    onMouseOver='onMes5(\"���C���^�E���ֈړ�\")' onMouseOut='onMes5(\"\")' alt=\"���C���^�E���ֈړ�\"></td></form>\n",
#koko2007/01/24

"�l��" => "<form method=POST action=\"./sugoroku_for_town/zinsei.cgi\"><td height=32 width=32><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=sex value=$sex><input type=hidden name=mode value=cont><input type=hidden name=yobidasi value=login_view><input type=hidden name=command value=select_com><input type=image src=\"$img_dir/zinsei.gif\"  onMouseOver='onMes5(\"�u�l���̃Q�[���v�ł��B�҂���������TOWN�̋�s�ɐU�荞�ނ��Ƃ��ł��܂��B\")' onMouseOut='onMes5(\"\")'></td></form>",

"����" => "<form method=POST action=\"gouseiya.cgi\"><input type=hidden name=mode value=\"gousei\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/gouseiyai.gif'  onMouseOver='onMes5(\"�������ĕi�������܂��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"����" => "<form method=POST action=\"auction.cgi\"><input type=hidden name=mode value=\"auction\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/auction.gif'  onMouseOver='onMes5(\"�������ł��B\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"���T" => "<form method=POST action=\"tokuten.cgi\"><input type=hidden name=mode value=\"tokuten\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/tokuten.gif'  onMouseOver='onMes5(\"���T\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�Q����" => "<form method=POST action=\"gamerand.cgi\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><td height=32 width=32><input type=image src='$img_dir/game.gif'  onMouseOver='onMes5(\"�Q�[�������h\")' onMouseOut='onMes5(\"\")'></td></form>\n",

"�Z��" => "<form method=POST action=\"jyusyo.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"jyusyo\"><input type=hidden name=name value=\"$name\"><input type=hidden name=pass value=\"$pass\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src='$img_dir/bil.gif' onMouseOver='onMes5(\"���X���Ђ����邱�Ƃ��o���܂�\")' onMouseOut='onMes5(\"\")'></td></form>\n",		#ver.1.40 2007/11/13

####�u�����܂Łv
);

################�p�[�c���̒�`�����܂�
}

sub kozin_house {
#�l�̉Ə���unit�n�b�V���ɑ��
	open(OI,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
	eval{ flock (OI, 1); }; #koko2007/06/16
	@ori_ie_hairetu = <OI>;
	foreach (@ori_ie_hairetu) {
			&ori_ie_sprit($_);
			$unit{"$ori_k_id"} = "<form method=POST action=\"original_house.cgi\"><td><input type=hidden name=mode value=\"houmon\"><input type=hidden name=ori_ie_id value=\"$ori_k_id\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$ori_ie_image\"   onMouseOver='onMes5(\"$ori_ie_setumei\")' onMouseOut='onMes5(\"\")' alt=\"$ori_ie_setumei\"></td></form>\n";		#ver.1.40
	}
	close(OI);
}

sub simaitosi {
#���̊X�ւ̃����N����unit�n�b�V���ɑ��
	$i=0;
	$i2=1;
	foreach (@town_hairetu) {
			$unit{"�X$i2"} = "<form method=POST action=\"$script\"><input type=hidden name=mode value=\"login_view\"><input type=hidden name=command value=\"mati_idou\"><td height=32 width=32><input type=hidden name=maemati value=\"$in{'town_no'}\"><input type=hidden name=town_no value=\"$i\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=image src=\"$img_dir/kousa_r.gif\"    onMouseOver='onMes5(\"$_�ֈړ�\")' onMouseOut='onMes5(\"\")' alt=\"$_�ֈړ�\"></td></form>\n"; #koko2007/01/24
			$i ++;
			$i2 ++;
	}
} #2006/04/24

# �d�Ԃňړ� #koko2007/04/14
sub simaitosi2 {
#���̊X�ւ̃����N����unit�n�b�V���ɑ��
	$i=0;
	$i2=1;
	foreach (@town_hairetu) {
			$unit{"�o�X$i2"} = "<form method=POST action=\"$script\"><input type=hidden name=mode value=\"login_view\"><input type=hidden name=command value=\"mati_idou2\"><td height=32 width=32><input type=hidden name=maemati value=\"$in{'town_no'}\"><input type=hidden name=town_no value=\"$i\"><input type=hidden name=mysec value=\"$in{'mysec'}\"><!-- koko2006/04/01 --><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=image src=\"$img_dir/Station.png\"  onMouseOver='onMes5(\"$_�֓d�Ԃňړ�\")' onMouseOut='onMes5(\"\")' alt=\"$_�֓d�Ԃňړ�\"></td></form>"; #koko2007/01/24
			$i ++;
			$i2 ++;
	}
}


sub admin_parts {
#�Ǘ��ҍ쐬BBS�ւ̃����N����unit�n�b�V���ɑ��
	$i=1;
	$i2=0;
	foreach (@admin_bbs_syurui) {
			$unit{"�f$i"} = "<form method=POST action=\"original_house.cgi\"><td height=32 width=32><input type=hidden name=mode value=\"normal_bbs\"><input type=hidden name=ori_ie_id value=\"admin\"><input type=hidden name=bbs_num value=\"$i2\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=image src=\"$img_dir/$admin_bbs_gazou[$i2]\"   onMouseOver='onMes5(\"$_\")' onMouseOut='onMes5(\"\")' alt=\"$_\"></td></form>\n";		#ver.1.40
			$i ++;
			$i2 ++;
	}
}

1;