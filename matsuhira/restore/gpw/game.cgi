#!/usr/local/bin/perl

# �����g���̃T�[�o�[�̃p�X�ɍ��킹�Ă��������B
#################################
# ���}���b�Z�[�W�p�@�ݒ�
#
# �����Ǘ��҂�ID�ԍ�
$kanrisya_id = "2207";
# �����Ǘ��Җ��O�B���X���Ă��͂��悤�ɓo�^���Ă��閼�O�������Ă��������B
$kanrisyaname = '����';#�o�^��ɖ��O�����Ă��������B
# ���}�R�����g
$m_comment = '�V�i�O�_�j�X�N�鍑�ւ悤����!<br>���͊Ǘ��l�̏���Ɛ\���܂��B<br>�܂��́uWORK�v�ŐE�Ƃɂ��Ă���A�uFOOD�v�ŐH�������Ă��������B<br>�i�E�Ƃɂ��Ȃ�������A�����H�ׂĂ��Ȃ��ꍇ�f�[�^�������ɍ폜����Ă��܂��̂Œ��ӁI�j<br>�ڂ����s�n�v�m�̋K�����ɂ��Ă�<A Href="http://www15.atpages.jp/g10works/cgi-bin/town3/nkeppo.html">�u���@�v</A>���������������B<br>�s���l�܂����菕���̗~�����Ƃ��͋߂��̐l��Ǘ��l�ɉ��������ǂ����B<br>��낵�����肢���܂��B';
# �Ǘ��҂ɓ͂����b�Z�[�W#koko2006/12/29 decode �� $in{'name'} �������ł͋�
# $my_m_comment = "$in{'name'}���񂪐V�K�o�^����A�V���������o�[�ɂȂ�܂����B";

# ���������t
$in_aikotoba = '';# 'irohaniho';  #�������t #koko2007/01/06

# �����_���Љ�ҏ���# 'yes';'no';'';�̎O��� #2/2 town_maker.cgi �ɂ�����B
$syokai = 'no';
# �Љ�҂ɏЉ�̎x�����B#koko2007/09/20
$syoukai_majin = 'no';
# eval{ flock (IN, 2); }; 2007/06/19
#################################

$this_script = 'game.cgi';
require './jcode.pl';
require './cgi-lib.pl';
require './town_ini.cgi';
require './town_lib.pl';
&decode;
#�����e�`�F�b�N
	if($mente_flag == 1 && $in{'admin_pass'} eq "" && $in{'mode'} ne ""){&error("$mente_message")}
$seigenyou_now_time = time;
#�������ԃ`�F�b�N
		$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $access_byou);
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("�܂��s���ł��܂���B����$ato_nanbyou�b���҂����������B")}
		
#��������
	if($in{'mode'} eq "battle"){&battle;}
	elsif($in{'mode'} eq "doukyo"){&doukyo;}
	elsif($in{'mode'} eq "c_league"){&c_league;}
	elsif($in{'mode'} eq "new"){&new;}
	elsif($in{'mode'} eq "data_hozon"){&data_hozon;}
	else{&error("�u�߂�v�{�^���ŊX�ɖ߂��Ă�������");}
exit;
	
#############�ȉ��T�u���[�`��
sub battle {
	open(IN,"< $logfile") || &error("Open Error : $logfile");
	eval{ flock (IN, 1); };
	@aite_erabi = <IN>;
	close(IN);
#	srand(time^$$);
	$randed= int (rand($#aite_erabi));
	$aite_erabi=splice(@aite_erabi,$randed,1);
	($aite_id) = split(/<>/,$aite_erabi);
	if ($aite_id eq "$k_id"){&message("�������肪������Ȃ������B�B","login_view");}
	&openAitelog ($aite_id);
	
	$aite_energy_max = int(($aite_looks/12) + ($aite_tairyoku/4) + ($aite_kenkou/4) + ($aite_speed/8) + ($aite_power/8) + ($aite_wanryoku/8) + ($aite_kyakuryoku/8));
	$aite_nou_energy_max = int(($aite_kokugo/6) + ($aite_suugaku/6) + ($aite_rika/6) + ($aite_syakai/6) + ($aite_eigo/6)+ ($aite_ongaku/6)+ ($aite_bijutu/6));
#�A�C�R��������Α��
	if ($kounyuu){$icon_hyouzi_a = "<img src=$kounyuu width=32 height=32 align=left>";}else{$icon_hyouzi_a = "";}
	if ($aite_kounyuu){$aite_icon_hyouzi_a = "<img src=$aite_kounyuu width=32 height=32 align=left>";}else{$aite_icon_hyouzi_a = "";}
	&header;
	print <<"EOM";
	<br><br><table width="600" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr align=center><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2 bgcolor=#ccff66 >
$icon_hyouzi_a$name����
</td></tr>
<tr><td align=right><span class=honbun3>���]�p���[</span>�F</td><td>$nou_energy</td></tr>
<tr><td align=right><span class=honbun3>�g�̃p���[</span>�F</td><td>$energy</td></tr>
<tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td align=center><span class=tyuu colspan=2>���@�]</span></td></tr>
<tr><td align=right><span class=honbun3>����</span>�F</td><td>$kokugo</td></tr>
<tr><td align=right><span class=honbun3>���w</span>�F</td><td>$suugaku</td></tr>
<tr><td align=right><span class=honbun3>����</span>�F</td><td>$rika</td></tr>
<tr><td align=right><span class=honbun3>�Љ�</span>�F</td><td>$syakai</td></tr>
<tr><td align=right><span class=honbun3>�p��</span>�F</td><td>$eigo</td></tr>
<tr><td align=right><span class=honbun3>���y</span>�F</td><td>$ongaku</td></tr>
<tr><td align=right><span class=honbun3>���p</span>�F</td><td>$bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>�g�@��</span></td></tr>
<tr><td  align=right nowrap><span class=honbun3>���b�N�X</span>�F</td><td>$looks</td></tr>
<tr><td align=right><span class=honbun3>�̗�</span>�F</td><td>$tairyoku</td></tr>
<tr><td align=right><span class=honbun3>���N</span>�F</td><td>$kenkou</td></tr>
<tr><td align=right nowrap><span class=honbun3>�X�s�[�h</span>�F</td><td>$speed</td></tr>
<tr><td align=right><span class=honbun3>�p���[</span>�F</td><td>$power</td></tr>
<tr><td align=right><span class=honbun3>�r��</span>�F</td><td>$wanryoku</td></tr>
<tr><td align=right><span class=honbun3>�r��</span>�F</td><td>$kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>���̑�</span></td>
<tr><td align=right><span class=honbun3>LOVE</span>�F</td><td>$love</td></tr>
<tr><td align=right><span class=honbun3>�ʔ���</span>�F</td><td>$unique</td></tr>
<tr><td align=right><span class=honbun3>�G�b�`</span>�F</td><td>$etti</td></tr>
</table>
	</td><td>
	<div class=tyuu>$aite_name����ƊX�ŏo������I</div><br><br>
	<div class=dai>Fight start !!</div>
	</td><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2 bgcolor=#ffcc99>
$aite_icon_hyouzi_a$aite_name����
</td></tr>
<tr><td align=right><span class=honbun3>���]�p���[</span>�F</td><td>$aite_nou_energy_max</td></tr>
<tr><td align=right><span class=honbun3>�g�̃p���[</span>�F</td><td>$aite_energy_max</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td colspan=2 align=center><span class=tyuu>���@�]</span></td></tr>
<tr><td align=right><span class=honbun3>����</span>�F</td><td>$aite_kokugo</td></tr>
<tr><td align=right><span class=honbun3>���w</span>�F</td><td>$aite_suugaku</td></tr>
<tr><td align=right><span class=honbun3>����</span>�F</td><td>$aite_rika</td></tr>
<tr><td align=right><span class=honbun3>�Љ�</span>�F</td><td>$aite_syakai</td></tr>
<tr><td align=right><span class=honbun3>�p��</span>�F</td><td>$aite_eigo</td></tr>
<tr><td align=right><span class=honbun3>���y</span>�F</td><td>$aite_ongaku</td></tr>
<tr><td align=right><span class=honbun3>���p</span>�F</td><td>$aite_bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>�g�@��</span></td></tr>
<tr><td  align=right nowrap><span class=honbun3>���b�N�X</span>�F</td><td>$aite_looks</td></tr>
<tr><td align=right><span class=honbun3>�̗�</span>�F</td><td>$aite_tairyoku</td></tr>
<tr><td align=right><span class=honbun3>���N</span>�F</td><td>$aite_kenkou</td></tr>
<tr><td align=right nowrap><span class=honbun3>�X�s�[�h</span>�F</td><td>$aite_speed</td></tr>
<tr><td align=right><span class=honbun3>�p���[</span>�F</td><td>$aite_power</td></tr>
<tr><td align=right><span class=honbun3>�r��</span>�F</td><td>$aite_wanryoku</td></tr>
<tr><td align=right><span class=honbun3>�r��</span>�F</td><td>$aite_kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>���̑�</span></td>
<tr><td align=right><span class=honbun3>LOVE</span>�F</td><td>$aite_love</td></tr>
<tr><td align=right><span class=honbun3>�ʔ���</span>�F</td><td>$aite_unique</td></tr>
<tr><td align=right><span class=honbun3>�G�b�`</span>�F</td><td>$aite_etti</td></tr>
</table>
	</td></tr></table>
EOM

	if ($speed > $aite_speed){$turn =1;}
	$sentou_kaisuu =0;
	foreach (1..50){
			print "<br><br><table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\" align=center class=yosumi><tr><td colspan=2>";
			if ($turn == 1){&kougeki (1,$name);			#�����̍U��
			}else{&kougeki (0,$aite_name);}			#����̍U��
			print <<"EOM";
			</td></tr>
			<tr><td align=left>
			<div class=tyuu>���]�p���[�F$nou_energy</div>
			<div class=tyuu>�g�̃p���[�F$energy</div>
			</td>
			<td align=right>
			<div class=tyuu>���]�p���[�F$aite_nou_energy_max</div>
			<div class=tyuu>�g�̃p���[�F$aite_energy_max</div>
			</td></tr></table>
EOM
			$sentou_kaisuu ++;
			if ($aite_energy_max <= 0){$win_flag=1;last;}
			if ($aite_nou_energy_max <= 0){$win_flag=2;last;}
			if ($energy <= 0){$win_flag=3;last;}
			if ($nou_energy <= 0){$win_flag=4;last;}
			if ($turn == 1){$turn = 0;} else {$turn = 1;}
	}
	print "<br><br>";
	if ($energy < 0){$energy = 0;}
	if ($nou_energy < 0){$nou_energy = 0;}
	$get_money=$sentou_kaisuu*300;
	if ($win_flag == 1) {
		$get_money *= 5;
		print "<div align=center style=\"color:#339933;font-size:14px;\">�����܂����I<br>�|��Ă���$aite_name����̍��z����<br>$get_money�~��D���܂����B</div>";
		$money += $get_money;
	}elsif($win_flag == 2){
		$get_money *= 5;
		print "<div align=center style=\"color:#339933;font-size:14px;\">�����܂����I<br>�l����̖͂���$aite_name����̍��z����<br>$get_money�~��D���܂����B</div>";
		$money += $get_money;
	}elsif($win_flag == 3){
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">�����Ă��܂��܂����B�B<br>�{���{���ɂȂ���$name����̍��z����<br>$get_money�~��D���܂����B</div>";
		$money -= $get_money;
	}elsif($win_flag == 4){
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">�����Ă��܂��܂����B�B<br>�ӎ��������낤�Ƃ���$name����̍��z����<br>$get_money�~��D���܂����B</div>";
		$money -= $get_money;
	}else{
		print "���������܂���ł����B�B";
	}
#�f�[�^�X�V
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
	&hooter("login_view","�߂�");
	exit;
}

sub kougeki {
#�U�����e�������_���őI��
		$battle_rand = int(rand(16))+1;
		print "<table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=center><tr align=center><td>";
##�����̍U���̏ꍇ
		if (@_[0] == 1){
			print "<div style=\"color:#339933;font-size:12px;\" align=left>@_[1]�̍U���I<br>";
#�U�����e
			&kougekinaiyou (1,$aite_name);
#���ʕ\��
			if ($damage eq "no_d"){
					print "<div style=\"color:#ff3300;font-size:12px;\" align=right>$return_naiyou</div>\n";
			}else{
					print "<div style=\"color:#339933;font-size:12px;\" align=right>$return_naiyou</div>\n";
					if ($battle_rand <= 8 || $battle_rand == 14){
						$aite_nou_energy_max -= $damage;
					}else{
						$aite_energy_max -= $damage;
					}
			}
			
##����̍U���̏ꍇ
		}else {
			print "<div style=\"color:#ff3300;font-size:12px;\" align=right>@_[1]�̍U���I<br>";
			&kougekinaiyou (0,$name);
#���ʕ\��
#�����ɂ����Ȃ��ꍇ
			if ($damage eq "no_d"){
					print "<div style=\"color:#339933;font-size:12px;\" align=left>$return_naiyou</div>\n";
			}else{
#�_���[�W���󂯂��ꍇ
					print "<div style=\"color:#ff3300;font-size:12px;\" align=left>$return_naiyou</div>\n";
#���]�_���[�W
					if ($battle_rand <= 8 || $battle_rand == 14){
						$nou_energy -= $damage;
					}else{
#���̃_���[�W
						$energy -= $damage;
					}
			}
		}
	print "</td></tr></table>";
}

###�U�����e���Ƃ̃_���[�W�����T�u���[�`��
sub kougekinaiyou {
# @_[0]��1�Ȃ玩���̍U���A0�Ȃ瑊��̍U��
	if (@_[0] == 1){$align_settei = "align=left";}else{$align_settei = "align=right";}
#����̍U��
		if ($battle_rand ==1){
			print "���̊������ǂ߂邩�H��@_[1]�ɕ��݊�����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],1);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͊��������ӂ������̂ł������蓚�����B�B";}
			else{$return_naiyou = "�u��A�ǂ߂Ȃ��B�B�v@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==2){
			print "������w�̖���@_[1]�����点�悤�Ƃ����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],2);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͐��w�����ӂ������̂Ō��ʂ����������B�B";}
			else{$return_naiyou = "����Ղ񂩂�Ղ񂾂���@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==3){
			print "���Ȃ̌�����������@_[1]�̓��h��U�����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],3);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͗��Ȃ����ӂ������̂Ō��ʂ����������B�B";}
			else{$return_naiyou = "������������@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==4){
			print "�L���ȗ��j�̎����̔N����@_[1]�Ɏ���U�߂����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],4);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͗��j���哾�ӂ������B�B";}
			else{$return_naiyou = "�ł���@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==5){
			print "�ˑR�p�������ׂ�o�����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],5);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]���������Ɖp��œ������B�B";}
			else{$return_naiyou = "�u�����Ɖp���׋����˂΁B�B�v��@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==6){
			print "�߂��ɂ������s�A�m�̌��Ղ�@���A���̉��K�͉��H�Ǝ��₵���I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],6);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͊ȒP�Ɏ���ɓ������B�B";}
			else{$return_naiyou = "�u��A�킩���B�B�v@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==7){
			print "���炷��ƌi�F��`����@_[1]�Ɍ������I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],7);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�́u���̉��肭�����I�v�Ɠf���̂Ă��B�B";}
			else{$return_naiyou = "�u���A���܂��B�B�v@_[1]��<span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==8){
			print "���b�N�X�ŏ�������I��@_[1]�ɔ������I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],8);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�́u�������ˁv�ƂԂ₢���B";}
			else{$return_naiyou = "�u���B�B�v@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==9){
			print "�̗͏����Ɏ�������</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],9);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�̗͑͂Ɏ��M���������B�B";}
			else{$return_naiyou = "@_[1]��<span style=\"font-size:18px\">$damage</span> �̓��̓I��J���󂯂��I";}
		}

		if ($battle_rand ==10){
			print "�f�����t�b�g���[�N��@_[1]��|�M���悤�Ƃ����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],11);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�̕����f���������B�B";}
			else{$return_naiyou = "@_[1]�͖|�M���� <span style=\"font-size:18px\">$damage</span> �̓��̓I��J���󂯂��I";}
		}

		if ($battle_rand ==11){
			print "�p���[��@_[1]�𓊂���΂����Ƃ����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],12);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͂����ƃp���[���������B�B";}
			else{$return_naiyou = "@_[1]�͓�����΂��� <span style=\"font-size:18px\">$damage</span> �̓��̓I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==12){
			print "@_[1]�Ƀp���`�𗁂т����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],13);
			if ($damage eq "no_d"){$return_naiyou = "������@_[1]�͌y���悯���B�B";}
			else{$return_naiyou = "@_[1]�� �p���`�𗁂�<span style=\"font-size:18px\">$damage</span> �̓��̓I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==13){
			print "@_[1]�ɏR�肩�������I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],14);
			if ($damage eq "no_d"){$return_naiyou = "������@_[1]�͂����Ƃ悯���B�B";}
			else{$return_naiyou = "@_[1]�� �R��𗁂�<span style=\"font-size:18px\">$damage</span> �̓��̓I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==14){
			print "�����Ă�����l�̎������n�߂��I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],15);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�͂����Ɨ��l�������Ă���ƌ������B�B";}
			else{$return_naiyou = "�u���A�����܂����B�B�v@_[1]�� <span style=\"font-size:18px\">$damage</span> �̐��_�I�_���[�W���󂯂��I";}
		}

		if ($battle_rand ==15){
			print "@_[1]���΂킹�A���̃X�L�Ɉꔭ���݂܂����悤�Ƃ����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],16);
			if ($damage eq "no_d"){$return_naiyou = "�u�܂��I�v��@_[1]�͈�R�����B�B";}
			else{$return_naiyou = "@_[1]�͏΂��]���A���̌��� <span style=\"font-size:18px\">$damage</span> �̃p���`����������I";}
		}
		
		if ($battle_rand ==16){
			print "�����̃G�b�`�Ŕ|�����閧�Z���I�����I</div><br>\n";
# iryoku_hantei (�U����,�U���̓��e)
			&iryoku_hantei (@_[0],17);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�̕����ꖇ����Ă������B�B";}
			else{$return_naiyou = "@_[1]�͖|�M���� <span style=\"font-size:18px\">$damage</span> �̓��̓I�_���[�W���󂯂��I";}
		}
}

#�З͔���T�u���[�`��
sub iryoku_hantei {
#�U���̓��e���Ƃ̔\�͒l
	$iryoku_hanteiti = @_[1] + 5;
	if (@_[0] == 1){
		$hantei_kakkati = $nouryoku_suuzi_hairetu[$iryoku_hanteiti]  - $aite_nouryoku_suuzi_hairetu[$iryoku_hanteiti] ;
	}else{
		$hantei_kakkati = $aite_nouryoku_suuzi_hairetu[$iryoku_hanteiti]  - $nouryoku_suuzi_hairetu[$iryoku_hanteiti] ;
	}
	if ($hantei_kakkati <= 0){
			$damage = "no_d";
	}else{
			$damage = "$hantei_kakkati";
	}
}

####�����l
sub doukyo {
		if ($chara_x_size == "" && $chara_y_size == ""){
			$chara_gazou_size = "";
			$c_size_comment = "";
		}else{
			$chara_gazou_size = "width=$chara_x_size height=$chara_y_size";
			$c_size_comment = "�摜�T�C�Y�͉�$chara_x_size�s�N�Z���A�c$chara_y_size�s�N�Z���ł��B";
		}
		$chara_settei_file="./member/$k_id/chara_ini.cgi";
			if (! -e $chara_settei_file){
				open(OIB,">$chara_settei_file") || &error("Write Error : $chara_settei_file");
				eval{ flock (OIB, 2); };
				chmod 0666,"$chara_settei_file";
				close(OIB);
			}
		open(CSF,"< $chara_settei_file") || &error("Open Error : $chara_settei_file");
		eval{ flock (CSF, 1); };
			$chara_settei_data = <CSF>;
			($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_point,$ch_yuusyoukai,$ch_kokugo,$ch_suugaku,$ch_rika,$ch_syakai,$ch_eigo,$ch_ongaku,$ch_bijutu,$ch_looks,$ch_tairyoku,$ch_kenkou,$ch_speed,$ch_power,$ch_wanryoku,$ch_kyakuryoku,$ch_love,$ch_unique,$ch_etti,$ch_energy,$ch_nou_energy,$ch_sintai,$ch_zunou,$ch_me_kokugo,$ch_me_suugaku,$ch_me_rika,$ch_me_syakai,$ch_me_eigo,$ch_me_ongaku,$ch_me_bijutu,$ch_me_looks,$ch_me_tairyoku,$ch_me_kenkou,$ch_me_speed,$ch_me_power,$ch_me_wanryoku,$ch_me_kyakuryoku,$ch_me_love,$ch_me_unique,$ch_me_etti,$ch_k_yobi3,$ch_k_yobi4,$ch_k_yobi5)= split(/<>/,$chara_settei_data);
		close(CSF);
		
#�L�����ݒ菈���̏ꍇ
		if ($in{'command'} eq "make_chara"){
			if (length($in{'ch_name'}) > 30) {&error("�L�����N�^�[�̖��O��30���ȓ��ł�");}
			$cgi_lib'maxdata = 51200;
			$MaxW = 80;	# ����
			$MaxH = 80;	# �c��
			if ($ch_k_id eq ""){$ch_k_id = $k_id;}
#koko2005/05/04
			if (!( $in{'ch_gazou'} =~ /http\:\/\/./) && $in{'ch_gazou'}){
				&error("http://�Ŏn�܂�A�h���X���w�肵�Ă��������B");
			}else {
				$ch_gazou = $in{'ch_gazou'}; #�ʒu��w�苖��
			}
			if ($in{'ch_name'}){ 
				$ch_name = $in{'ch_name'};
				&c_ne_chra; #�V���������
			}
#kokoend
			if ($ch_oyaname eq ""){$ch_oyaname = $name;}
			#if ($in{'ch_gazou'}){$ch_gazou = $in{'ch_gazou'};}
			if ($in{'ch_kokugo'} && $kokugo > $in{'ch_kokugo'}) { $ch_kokugo += $in{'ch_kokugo'}; $message_in .= "����p�����[�^��$in{'ch_kokugo'}�����܂����B<br>"; $hikukane += $in{'ch_kokugo'}; $kokugo -=$in{'ch_kokugo'}; }
			if ($in{'ch_suugaku'} && $suugaku > $in{'ch_suugaku'}) { $ch_suugaku += $in{'ch_suugaku'}; $message_in .= "���w�p�����[�^��$in{'ch_suugaku'}�����܂����B<br>"; $hikukane += $in{'ch_suugaku'}; $suugaku -=$in{'ch_suugaku'};}
			if ($in{'ch_rika'} && $rika > $in{'ch_rika'}) { $ch_rika += $in{'ch_rika'}; $message_in .= "���ȃp�����[�^��$in{'ch_rika'}�����܂����B<br>"; $hikukane += $in{'ch_rika'}; $rika -=$in{'ch_rika'};}
			if ($in{'ch_syakai'} && $syakai > $in{'ch_syakai'}) { $ch_syakai += $in{'ch_syakai'}; $message_in .= "�Љ�p�����[�^��$in{'ch_rika'}�����܂����B<br>"; $hikukane += $in{'ch_syakai'}; $syakai -=$in{'ch_syakai'};}
			if ($in{'ch_eigo'} && $eigo > $in{'ch_eigo'}) { $ch_eigo += $in{'ch_eigo'}; $message_in .= "�p��p�����[�^��$in{'ch_eigo'}�����܂����B<br>"; $hikukane += $in{'ch_eigo'}; $eigo -=$in{'ch_eigo'};}
			if ($in{'ch_ongaku'} && $ongaku > $in{'ch_ongaku'}) { $ch_ongaku += $in{'ch_ongaku'}; $message_in .= "���y�p�����[�^��$in{'ch_ongaku'}�����܂����B<br>"; $hikukane += $in{'ch_ongaku'}; $ongaku -=$in{'ch_ongaku'};}
			if ($in{'ch_bijutu'} && $bijutu > $in{'ch_bijutu'}) { $ch_bijutu += $in{'ch_bijutu'}; $message_in .= "���p�p�����[�^��$in{'ch_bijutu'}�����܂����B<br>"; $hikukane += $in{'ch_bijutu'}; $bijutu -=$in{'ch_bijutu'};}
			if ($in{'ch_looks'} && $looks > $in{'ch_looks'}) { $ch_looks += $in{'ch_looks'}; $message_in .= "���b�N�X�p�����[�^��$in{'ch_looks'}�����܂����B<br>"; $hikukane += $in{'ch_looks'}; $looks -=$in{'ch_looks'};}
			if ($in{'ch_tairyoku'} && $tairyoku > $in{'ch_tairyoku'}) { $ch_tairyoku += $in{'ch_tairyoku'}; $message_in .= "�̗̓p�����[�^��$in{'ch_tairyoku'}�����܂����B<br>"; $hikukane += $in{'ch_tairyoku'}; $tairyoku -=$in{'ch_tairyoku'};}
			if ($in{'ch_kenkou'} && $kenkou > $in{'ch_kenkou'}) { $ch_kenkou += $in{'ch_kenkou'}; $message_in .= "���N�p�����[�^��$in{'ch_kenkou'}�����܂����B<br>"; $hikukane += $in{'ch_kenkou'}; $kenkou -=$in{'ch_kenkou'};}
			if ($in{'ch_speed'} && $speed > $in{'ch_speed'}) { $ch_speed += $in{'ch_speed'}; $message_in .= "�X�s�[�h�p�����[�^��$in{'ch_speed'}�����܂����B<br>"; $hikukane += $in{'ch_speed'}; $speed -=$in{'ch_speed'};}
			if ($in{'ch_power'} && $power > $in{'ch_power'}) { $ch_power += $in{'ch_power'}; $message_in .= "�p���[�p�����[�^��$in{'ch_power'}�����܂����B<br>"; $hikukane += $in{'ch_power'}; $power -=$in{'ch_power'};}
			if ($in{'ch_wanryoku'} && $wanryoku > $in{'ch_wanryoku'}) { $ch_wanryoku += $in{'ch_wanryoku'}; $message_in .= "�r�̓p�����[�^��$in{'ch_wanryoku'}�����܂����B<br>"; $hikukane += $in{'ch_wanryoku'}; $wanryoku -=$in{'ch_wanryoku'};}
			if ($in{'ch_kyakuryoku'} && $kyakuryoku > $in{'ch_kyakuryoku'}) { $ch_kyakuryoku += $in{'ch_kyakuryoku'}; $message_in .= "�r�̓p�����[�^��$in{'ch_kyakuryoku'}�����܂����B<br>"; $hikukane += $in{'ch_kyakuryoku'}; $kyakuryoku -=$in{'ch_kyakuryoku'};}
			if ($in{'ch_love'} && $love > $in{'ch_love'}) { $ch_love += $in{'ch_love'}; $message_in .= "LOVE�p�����[�^��$in{'ch_love'}�����܂����B<br>"; $hikukane += $in{'ch_love'}; $love -=$in{'ch_love'};}
			if ($in{'ch_unique'} && $unique > $in{'ch_unique'}) { $ch_unique += $in{'ch_unique'}; $message_in .= "�ʔ����p�����[�^��$in{'ch_unique'}�����܂����B<br>"; $hikukane += $in{'ch_unique'}; $unique -=$in{'ch_unique'};}
			
			if ($in{'ch_etti'} && $etti > $in{'ch_etti'}) { $ch_etti += $in{'ch_etti'}; $message_in .= "�G�b�`�p�����[�^��$in{'ch_etti'}�����܂����B<br>"; $hikukane += $in{'ch_etti'}; $etti -=$in{'ch_etti'};}
			
			if($hikukane =~ /[^0-9]/){&error("���l���s�K�؂ł�");}
			if ($hikukane < 0){&error("���l���s�K�؂ł�");}
			if ($hikukane != 0){
				$message_in .= "$hikukane���~�̂�����������܂����B<br>";
			}
#koko 2005/04/16
			$c_kane_bank = $hikukane*10000;
			if ($k_sousisan < $c_kane_bank){&error("�����Y�ȏ�͎g���܂���");}
			if ($in{'siharaihouhou'} ne "����"){
				$bank -= $hikukane*10000;
				if ($c_kane_bank){ #koko 2005/05/05
					&kityou_syori("�N���W�b�g�x�����i�b���[�O�x�����j","$c_kane_bank","",$bank,"��");
				}
			}else{
				if ($money < $hikukane*10000){&error("����������܂���");}
				$money -= $hikukane*10000;
			}
			#if ($money < $hikukane*10000){&error("����������܂���");}
			#kokoend
			
			if ($in{'ch_me_kokugo'}) { $ch_me_kokugo = "$in{'ch_me_kokugo'}";}
			if ($in{'ch_me_suugaku'}) { $ch_me_suugaku = "$in{'ch_me_suugaku'}";}
			if ($in{'ch_me_rika'}) { $ch_me_rika = "$in{'ch_me_rika'}";}
			if ($in{'ch_me_syakai'}) { $ch_me_syakai = "$in{'ch_me_syakai'}";}
			if ($in{'ch_me_eigo'}) { $ch_me_eigo = "$in{'ch_me_eigo'}";}
			if ($in{'ch_me_ongaku'}) { $ch_me_ongaku = "$in{'ch_me_ongaku'}";}
			if ($in{'ch_me_bijutu'}) { $ch_me_bijutu = "$in{'ch_me_bijutu'}";}
			if ($in{'ch_me_looks'}) { $ch_me_looks = "$in{'ch_me_looks'}";}
			if ($in{'ch_me_tairyoku'}) { $ch_me_tairyoku = "$in{'ch_me_tairyoku'}";}
			if ($in{'ch_me_kenkou'}) { $ch_me_kenkou = "$in{'ch_me_kenkou'}";}
			if ($in{'ch_me_speed'}) { $ch_me_speed = "$in{'ch_me_speed'}";}
			if ($in{'ch_me_power'}) { $ch_me_power = "$in{'ch_me_power'}";}
			if ($in{'ch_me_wanryoku'}) { $ch_me_wanryoku = "$in{'ch_me_wanryoku'}";}
			if ($in{'ch_me_kyakuryoku'}) { $ch_me_kyakuryoku = "$in{'ch_me_kyakuryoku'}";}
			if ($in{'ch_me_love'}) { $ch_me_love = "$in{'ch_me_love'}";}
			if ($in{'ch_me_unique'}) { $ch_me_unique = "$in{'ch_me_unique'}";}
			if ($in{'ch_me_etti'}) { $ch_me_etti = "$in{'ch_me_etti'}";}
			if  ($message_in eq ""){$message_in .= "�ύX���܂����B";}

#			if ($in{'upfile'}) { &UpFile; }
#�p���[��MAX�l�v�Z
	$ch_sintai = int(($ch_looks/10) + ($ch_tairyoku/10) + ($ch_kenkou/10) + ($ch_speed/10) + ($ch_power/10) + ($ch_wanryoku/10) + ($ch_kyakuryoku/10)+ ($ch_etti/10));
	$ch_zunou = int(($ch_kokugo/10) + ($ch_suugaku/10) + ($ch_rika/10) + ($ch_syakai/10) + ($ch_eigo/10)+ ($ch_ongaku/10)+ ($ch_bijutu/10)+ ($ch_love/10)+ ($ch_unique/10));
	
			$make_ch_temp ="$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_point<>$ch_yuusyoukai<>$ch_kokugo<>$ch_suugaku<>$ch_rika<>$ch_syakai<>$ch_eigo<>$ch_ongaku<>$ch_bijutu<>$ch_looks<>$ch_tairyoku<>$ch_kenkou<>$ch_speed<>$ch_power<>$ch_wanryoku<>$ch_kyakuryoku<>$ch_love<>$ch_unique<>$ch_etti<>$ch_energy<>$ch_nou_energy<>$ch_sintai<>$ch_zunou<>$ch_me_kokugo<>$ch_me_suugaku<>$ch_me_rika<>$ch_me_syakai<>$ch_me_eigo<>$ch_me_ongaku<>$ch_me_bijutu<>$ch_me_looks<>$ch_me_tairyoku<>$ch_me_kenkou<>$ch_me_speed<>$ch_me_power<>$ch_me_wanryoku<>$ch_me_kyakuryoku<>$ch_me_love<>$ch_me_unique<>$ch_me_etti<>$ch_k_yobi3<>$ch_k_yobi4<>$ch_k_yobi5";
	&lock;
	open(MTLO,">$chara_settei_file") || &error("Write Error : $chara_settei_file");
	eval{ flock (MTLO, 2); };
	print MTLO $make_ch_temp;
	close(MTLO);
	&unlock;
#	$money -= $hikukane * 10000;#koko2005/04/16
	$k_sousisan = $money + $bank + $super_teiki - ($loan_nitigaku * $loan_kaisuu);#koko2005/04/16
					&temp_routin;
					&log_kousin($my_log_file,$k_temp);
	&message("$message_in","doukyo","game.cgi");
		}		#�쐬�����̏ꍇ�̕�
	
#�R�����g�̏�����
	if ($ch_me_kokugo eq ""){$ch_me_kokugo = "���̊������ǂ߂邩�H";}
	if ($ch_me_suugaku eq ""){$ch_me_suugaku = "���̐��w�̓������킩�邩�H";}
	if ($ch_me_rika eq ""){$ch_me_rika = "���̌������l�����̂͒N���m���Ă邩�H";}
	if ($ch_me_syakai eq ""){$ch_me_syakai = "���̎����͉��N�ɋN�������m���Ă邩�H";}
	if ($ch_me_eigo eq ""){$ch_me_eigo = "���̉p�P��̈Ӗ���m���Ă邩�H";}
	if ($ch_me_ongaku eq ""){$ch_me_ongaku = "���̋Ȃ���Ȃ����̂͒N���m���Ă邩�H";}
	if ($ch_me_bijutu eq ""){$ch_me_bijutu = "���̊G�����Ă݂�I";}
	if ($ch_me_looks eq ""){$ch_me_looks = "���b�N�X�ŏ������I";}
	if ($ch_me_tairyoku eq ""){$ch_me_tairyoku = "�̗͂ŏ�������I";}
	if ($ch_me_kenkou eq ""){$ch_me_kenkou = "���N�ɂ͎��M�����邼�I";}
	if ($ch_me_speed eq ""){$ch_me_speed = "���̃X�s�[�h�ɂ��Ă����邩�ȁH";}
	if ($ch_me_power eq ""){$ch_me_power = "�^�b�N���ŏ������I";}
	if ($ch_me_wanryoku eq ""){$ch_me_wanryoku = "�r���o�ŏ������I";}
	if ($ch_me_kyakuryoku eq ""){$ch_me_kyakuryoku = "�L�b�N�������������Ă��I";}
	if ($ch_me_love eq ""){$ch_me_love = "���̐[���ł͕����Ȃ����I";}
	if ($ch_me_unique eq ""){$ch_me_unique = "���̃M���O�ǂ��H";}
	if ($ch_me_etti eq ""){$ch_me_etti = "�G�b�`�ł͕����Ȃ��I";}
#��ʕ\��
		if ($ch_gazou){$charaimage_gazou = "<img src=$ch_gazou $chara_gazou_size>";}
		else{$charaimage_gazou = "";}
		&header(item_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td bgcolor=#ffffff>�����ł͎��������̃L�����N�^�[���쐬���邱�Ƃ��ł��܂��B�L�����N�^�[�͎����̃p�����[�^�[�Ƃ����𓊓����邱�ƂŐ������܂��B<br>�ŋ��̃L�����N�^�[���쐬���āuC���[�O�v�ɎQ�����܂��傤�B<br>�i�����I�ɂ͎����̉ƂɃL�����̃R�[�i�[���ł��ė��K�҂Ƃ̂��Ƃ肪�ł���悤�ɂȂ�\\��ł��j</td>
	<td  bgcolor=#333333 align=center width=200><img src="$img_dir/chara_tytle.gif"></td>
	</tr></table><br>
EOM
	if ($in{'command'} eq ""){

#���L���`�F�b�N koko 2005/04/16
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(MK,"< $monokiroku_file") || &error("�����̍w�����t�@�C�����J���܂���");
	eval{ flock (MK, 1); };
	@my_kounyuu_list =<MK>;
	close(MK);
	foreach (@my_kounyuu_list){
		&syouhin_sprit ($_);
		if ($syo_kouka eq "�N���W�b�g"){
			if ($syo_taikyuu - (int ((time - $syo_kounyuubi) / (60*60*24)))){
				$siharai_houhou .= "<option value=\"$syo_hinmoku\">$syo_hinmoku</option>";
			}
		}
	}
	#kokoend

	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="doukyo">
	<input type=hidden name=command value="make_chara">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	
		<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
		<tr><td>
		<div align=center>
		$charaimage_gazou<br>
		<div class=honbun2>$ch_name</div><br>
		���̗ǂ��F$ch_zunou<br>
		�g�̔\\�́F$ch_sintai
		</div>
	
	</td><td>
	<div class=honbun2>���L�����̖��O�i�S�p15�����ȓ��j</div>�������ύX���ł��܂��B<br>
	<input type=text size=30 name=ch_name value=$ch_name><br><br>
	
	<div class=honbun2>���L�����N�^�[�摜</div>�ihttp://�`�Ŏn�܂���URL�B$c_size_comment ���摜�͂Ȃ��Ă��\\���܂���B�j<br>�������ύX���ł��܂��B<br>
	<!--<input type=file name="upfile" size=30><br>-->
	<input type=text name="ch_gazou" size=60 value=$ch_gazou><br><br>
	
	<div class=honbun2>���p�����[�^�[�A�b�v</div>
	���͂������l���̃p�����[�^�[���������������A����ɂ��̐��l�~�P���~�̔�p��������܂��B<br>
	�L�����N�^�[�͗^����ꂽ���l���̃p�����[�^�[���オ��܂��B<br>
	<table border="0"><tr>
	<td>����</td><td><input type=text name="ch_kokugo" size=10></td></td>
	<td>���w</td><td><input type=text name="ch_suugaku" size=10></td>
	<td>����</td><td><input type=text name="ch_rika" size=10></td>
	<td>�Љ�</td><td><input type=text name="ch_syakai" size=10></td>
	<td>�p��</td><td><input type=text name="ch_eigo" size=10></td></tr><tr>
	<td>���y</td><td><input type=text name="ch_ongaku" size=10></td>
	<td>���p</td><td><input type=text name="ch_bijutu" size=10></td>
	<td>���b�N�X</td><td><input type=text name="ch_looks" size=10></td>
	<td>�̗�</td><td><input type=text name="ch_tairyoku" size=10></td>
	<td>���N</td><td><input type=text name="ch_kenkou" size=10></td></tr><tr>
	<td>�X�s�[�h</td><td><input type=text name="ch_speed" size=10></td>
	<td>�p���[</td><td><input type=text name="ch_power" size=10></td>
	<td>�r��</td><td><input type=text name="ch_wanryoku" size=10></td>
	<td>�r��</td><td><input type=text name="ch_kyakuryoku" size=10></td>
	<td>LOVE</td><td><input type=text name="ch_love" size=10></td></tr><tr>
	<td>�ʔ���</td><td><input type=text name="ch_unique" size=10></td>
	<td>�G�b�`</td><td><input type=text name="ch_etti" size=10>
	</tr></table>

	</td><td width=150>
	<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;" bgcolor=#ffffcc width=100%>
<td colspan=2 align=center><span class=tyuu>���@�]</span></td></tr>
<tr><td align=right><span class=honbun5>����</span>�F</td><td align=right>$ch_kokugo</td></tr>
<tr><td align=right><span class=honbun5>���w</span>�F</td><td align=right>$ch_suugaku</td></tr>
<tr><td align=right><span class=honbun5>����</span>�F</td><td align=right>$ch_rika</td></tr>
<tr><td align=right><span class=honbun5>�Љ�</span>�F</td><td align=right>$ch_syakai</td></tr>
<tr><td align=right><span class=honbun5>�p��</span>�F</td><td align=right>$ch_eigo</td></tr>
<tr><td align=right><span class=honbun5>���y</span>�F</td><td align=right>$ch_ongaku</td></tr>
<tr><td align=right><span class=honbun5>���p</span>�F</td><td align=right>$ch_bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>�g�@��</span></td></tr>
<tr><td  align=right><span class=honbun5>���b�N�X</span>�F</td><td align=right>$ch_looks</td></tr>
<tr><td align=right><span class=honbun5>�̗�</span>�F</td><td align=right>$ch_tairyoku</td></tr>
<tr><td align=right><span class=honbun5>���N</span>�F</td><td align=right>$ch_kenkou</td></tr>
<tr><td align=right><span class=honbun5>�X�s�[�h</span>�F</td><td align=right>$ch_speed</td></tr>
<tr><td align=right><span class=honbun5>�p���[</span>�F</td><td align=right>$ch_power</td></tr>
<tr><td align=right><span class=honbun5>�r��</span>�F</td><td align=right>$ch_wanryoku</td></tr>
<tr><td align=right><span class=honbun5>�r��</span>�F</td><td align=right>$ch_kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>���̑�</span></td>
<tr><td align=right><span class=honbun5>LOVE</span>�F</td><td align=right>$ch_love</td></tr>
<tr><td align=right><span class=honbun5>�ʔ���</span>�F</td><td align=right>$ch_unique</td></tr>
<tr><td align=right><span class=honbun5>�G�b�`</span>�F</td><td align=right>$ch_etti</td></tr>
</table>
	</td></tr>
	<tr><td colspan=3>
	<div align=center>
�x���� <select name="siharaihouhou">$siharai_houhou<option value="����">����</option></select><!-- koko -->

	<input type=submit value=" O K "></div>
	</td></tr></table>
	</form>
	
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="doukyo">
	<input type=hidden name=command value="com_henkou">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�R�����g�ύX�t�H�[���o��"></form></div>
	
EOM
	}
	
	if ($in{'command'} eq "com_henkou"){
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="doukyo">
	<input type=hidden name=command value="make_chara">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td>
	<div class=honbun2>�������Ƃ��̃R�����g</div>
	�e�\\�͂��Ƃɂ��̔\\�͂ŏ������鎞�Ɍ����R�����g���L�����Ă��������B��40���ȓ��i���̃t�H�[���̒����Ɏ��܂�悤�Ɂj<br><br>
	<table border="0"><tr>
	<td>����</td><td><input type=text name="ch_me_kokugo" size=80 value=$ch_me_kokugo></td></td></tr><tr>
	<td>���w</td><td><input type=text name="ch_me_suugaku" size=80 value=$ch_me_suugaku></td></tr><tr>
	<td>����</td><td><input type=text name="ch_me_rika" size=80 value=$ch_me_rika></td></tr><tr>
	<td>�Љ�</td><td><input type=text name="ch_me_syakai" size=80 value=$ch_me_syakai></td></tr><tr>
	<td>�p��</td><td><input type=text name="ch_me_eigo" size=80 value=$ch_me_eigo></td></tr><tr>
	<td>���y</td><td><input type=text name="ch_me_ongaku" size=80 value=$ch_me_ongaku></td></tr><tr>
	<td>���p</td><td><input type=text name="ch_me_bijutu" size=80 value=$ch_me_bijutu></td></tr><tr>
	<td>���b�N�X</td><td><input type=text name="ch_me_looks" size=80 value=$ch_me_looks></td></tr><tr>
	<td>�̗�</td><td><input type=text name="ch_me_tairyoku" size=80 value=$ch_me_tairyoku></td></tr><tr>
	<td>���N</td><td><input type=text name="ch_me_kenkou" size=80 value=$ch_me_kenkou></td></tr><tr>
	<td>�X�s�[�h</td><td><input type=text name="ch_me_speed" size=80 value=$ch_me_speed></td></tr><tr>
	<td>�p���[</td><td><input type=text name="ch_me_power" size=80 value=$ch_me_power></td></tr><tr>
	<td>�r��</td><td><input type=text name="ch_me_wanryoku" size=80 value=$ch_me_wanryoku></td></tr><tr>
	<td>�r��</td><td><input type=text name="ch_me_kyakuryoku" size=80 value=$ch_me_kyakuryoku></td></tr><tr>
	<td>LOVE</td><td><input type=text name="ch_me_love" size=80 value=$ch_me_love></td></tr><tr>
	<td>�ʔ���</td><td><input type=text name="ch_me_unique" size=80 value=$ch_me_unique></td></tr><tr>
	<td>�G�b�`</td><td><input type=text name="ch_me_etti" size=80 value=$ch_me_etti></td>
	</tr></table>
	<div align=center><input type=submit value=" �R�����g�ύX "></div></form><br><br>
	<div align=center><a href="javascript:history.back()"> [�O�̉�ʂɖ߂�] </a></div>
	</td></tr></table>
EOM
	}


		&hooter("login_view","�߂�");
		exit;
}
###�L�����Ⴂ�@koko 2005/05/04
sub c_ne_chra{
	open(IN,"< $doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	eval{ flock (IN, 1); };
	$league_meisai = <IN>;
	@aite_erabi = <IN>;
	close(IN);
	$i = 0;
	foreach (@aite_erabi){
		my ($ch_k_id,$ch_name0,$ch_oyaname,$ch_gazou0,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($in{'name'} eq $ch_oyaname){
			$aite_erabi[$i] = "$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_kati<>$ch_make<>$ch_hikiwake<>$ch_yuusyou<>$ch_lasttime<>$ch_yobi1<>$ch_yobi2<>$ch_yobi3<>$ch_yobi4<>$ch_yobi5<>$ch_yobi6<>\n";
		}
		$i++;
	}

	@new_aite_erabi = @aite_erabi;
	unshift (@new_aite_erabi,$league_meisai);
	&lock;
	open(OUT,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	eval{ flock (OUT, 2); };
	print OUT @new_aite_erabi;
	close(OUT);			
	&unlock;
}
#kokoend

####�b���[�O
sub c_league {
		if ($chara_x_size == "" && $chara_y_size == ""){
			$chara_gazou_size = "";
			$c_size_comment = "";
		}else{
			$chara_gazou_size = "width=$chara_x_size height=$chara_y_size";
			$c_size_comment = "�摜�T�C�Y�͉�$chara_x_size�s�N�Z���A�c$chara_y_size�s�N�Z���ł��B";
		}
		open(IN,"< $doukyo_logfile") || &error("Open Error : $doukyo_logfile");
		eval{ flock (IN, 1); };
		$league_meisai = <IN>;
		@aite_erabi = <IN>;
		close(IN);
		$now_time= time;
#�Q�[�����׏�����
		if ($league_meisai eq ""){
			&lock;
			$league_meisai = "$now_time<>1<>\n";
			open(OUT,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
			eval{ flock (OUT, 2); };
			print OUT $league_meisai;
			close(OUT);
			&unlock;
		}
		($start_time,$nankai_taikai)= split(/<>/,$league_meisai);
		$nannitime = int(($now_time - $start_time) / (60*60*24)) + 1;
		if ($nannitime > $c_nissuu){&taikai_syokika;}
		
#�����̏ꍇ
	if ($in{'command'}eq "game") {
		&lock;
#�����̃L�����f�[�^���J���ĕϐ��ɓ����
	$chara_settei_file="./member/$k_id/chara_ini.cgi";
	open(CSF,"< $chara_settei_file") || &error("�L�������쐬���Ă���łȂ��Ǝ����͂ł��܂���");
	eval{ flock (CSF, 1); };
	$chara_settei_data = <CSF>;
	@my_chara_para =  split(/<>/,$chara_settei_data);
	if ($chara_settei_data eq ""){&error("�L�������쐬���Ă���łȂ��Ǝ����͂ł��܂���");}
	close(CSF);
#�o�^����Ă���L����ID�Ŕz��쐬�B���o�^�Ȃ�o�^
	$zibun_hazusi = 0;
	@taisen_list = (); #koko2007/07/16
	@all_taisen_list = (); #koko2007/07/16
	foreach (@aite_erabi){
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime)= split(/<>/);
#���������������玎�����X�g���玩�����͂����B
		if(!(-e "./member/$ch_k_id/chara_ini.cgi")){next;} #koko2007/10/13
		if ($name eq $ch_oyaname){
			if ($now_time - $ch_lasttime < 60 * $c_siai_kankaku){&error("�܂��O��̎����̔�ꂪ�c���Ă��܂��B");}
			$my_genzaino_joukyou = "$_";		#�����̏󋵂�ϐ��ɓ���Ă���
			$zibun_hazusi = 1;
			next;
		}
		push (@taisen_list,$ch_k_id);
		push (@all_taisen_list,$_);
	}
	if ($zibun_hazusi == 0){&c_league_touroku($chara_settei_data);}
	@nitteicheck = split(/<>/,$my_genzaino_joukyou);
	if ($nitteicheck[4] + $nitteicheck[5] + $nitteicheck[6] >= $c_siaisuu){&error("�S�����������I�����Ă��܂��B");}
	$ch_randed=int(rand($#taisen_list));
	$aite_kettei =splice(@taisen_list,$ch_randed,1);
#koko2007/10/13
	if (0 == int(rand(3))){$aite_kettei = $k_id; $manera =1;}
#	if ($aite_kettei eq ""){&message("�������肪������Ȃ������B�B","login_view");}#koko 2005/04/17 c_league
	if ($aite_kettei eq ""){$aite_kettei = $k_id; $manera =1;}
#	if ($aite_kettei eq "$k_id"){&message("�������肪������Ȃ������B�B","login_view");}#koko 2005/04/17 c_league
#	if ($aite_kettei eq "$k_id"){$aite_kettei = $k_id; $manera =1;}#koko 2005/04/17 c_league koko2007/10/13
#����̃L�����f�[�^���J���ĕϐ��ɓ����
	$aite_settei_file="./member/$aite_kettei/chara_ini.cgi";
	if(!(-e $aite_settei_file)){$aite_settei_file="./member/$k_id/chara_ini.cgi"; $manera =1;}
#end2007/10/13
	open(ASF,"< $aite_settei_file") || &error("�ΐ푊��̓s���ɂ�莎���͉����ƂȂ�܂���/member/$aite_kettei/chara_ini.cgi�B1");
	eval{ flock (ASF, 1); };
	$aite_settei_data = <ASF>;
	@aite_chara_para =  split(/<>/,$aite_settei_data);
	if ($aite_settei_data eq ""){&error("�ΐ푊��̓s���ɂ�莎���͉����ƂȂ�܂����B2");}
	close(ASF);
#�L�����摜������Εϐ��ɑ��
#koko2007/10/13
	if($manera){
		$aite_chara_para[1] = "�܂˂�[$aite_chara_para[1]";
		$aite_chara_para[2] = "�܂˂�[$aite_chara_para[2]";
	}
#end2007/10/13
	if ($my_chara_para[3]){
		$my_chara_image = "<img src=$my_chara_para[3] $chara_gazou_size>";
	}else{$my_chara_image = "";}
	if ($aite_chara_para[3]){
		$aite_chara_image = "<img src=$aite_chara_para[3] $chara_gazou_size>";
	}else{$aite_chara_image = "";}
	
	&header(item_style);
#�L�����̃p���[�i�̗́j���Z�o
	$my_chara_power = $my_chara_para[26] + $my_chara_para[25];
	$aite_chara_power = $aite_chara_para[26] + $aite_chara_para[25];
	print <<"EOM";
	<br><br><table width="600" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr align=center><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2>
$my_chara_para[2]�̃L�����N�^�[<br>
$my_chara_para[1]<br>
$my_chara_image
</td></tr>
<tr><td align=center><span class=honbun3>���̗ǂ�</span>�F</td><td>$my_chara_para[26]</td></tr>
<tr><td align=center><span class=honbun3>�g�̔\\��</span>�F</td><td>$my_chara_para[25]</td></tr>
</table>
	</td><td>
	<div class=tyuu>$aite_chara_para[1]�Ƃ̎������n�܂����I</div><br><br>
	</td><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2>
$aite_chara_para[2]�̃L�����N�^�[<br>
$aite_chara_para[1]<br>
$aite_chara_image
</td></tr>
<tr><td align=center><span class=honbun3>���̗ǂ�</span>�F</td><td>$aite_chara_para[26]</td></tr>
<tr><td align=center><span class=honbun3>�g�̔\\��</span>�F</td><td>$aite_chara_para[25]</td></tr>
</table>
	</td></tr></table>
EOM

	if ($my_chara_para[16] > $aite_chara_para[16]){$turn =1;}
	$sentou_kaisuu =0;
	foreach (1..25){
			print "<br><br><table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\" align=center class=yosumi><tr><td colspan=2>";
			if ($turn == 1){&ch_kougeki (1,$my_chara_para[1]);			#�����̍U��
			}else{&ch_kougeki (0,$aite_chara_para[1]);}			#����̍U��
			print <<"EOM";
			</td></tr>
			<tr><td align=left>
			<div class=tyuu>�G�l���M�[�F$my_chara_power</div>
			</td>
			<td align=right>
			<div class=tyuu>�G�l���M�[�F$aite_chara_power</div>
			</td></tr></table>
EOM
			$sentou_kaisuu ++;
			if ($aite_chara_power <= 0){$win_flag=1;last;}
			if ($my_chara_power <= 0){$win_flag=2;last;}
			if ($turn == 1){$turn = 0;} else {$turn = 1;}
	}
	print "<br><br>";
	
#��ɓ���Ă����������̏󋵂�split
	($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/,$my_genzaino_joukyou);
#ch_yobi1���Ō�̑ΐ�󋵁@ch_yobi2���l���|�C���g�@ch_yobi3���O�񏟂��@ch_yobi4���O�񕉂��@ch_yobi5���O���������

#�������ꍇ
	if ($win_flag == 1) {
		$ch_kati ++;
	#�Ō�̃o�g���R�����g
		$ch_yobi1 = "<td align=center>$my_chara_para[1] vs $aite_chara_para[1]</td><td align=center>$my_chara_para[1]</td><td>$my_chara_para[$battle_naiyou_hanbetu]</td>";
		print "<div align=center style=\"color:#339933;font-size:14px;\">�������������߂܂����I</div>";
#koko 2005/04/17
		$c_mouke = $dameegitame * 2;
		if(!$c_mouke){$c_mouke = 100;}
		print "<div align=center style=\"color:#339933;font-size:14px;\">$c_mouke�~��ɓ��ꂽ�B</div>";
#kokoend
#�������ꍇ
	}elsif($win_flag == 2){
	#�Ō�̃o�g���R�����g
		$ch_yobi1 = "<td align=center>$my_chara_para[1] vs $aite_chara_para[1]</td><td align=center>$aite_chara_para[1]</td><td>$aite_chara_para[$battle_naiyou_hanbetu]</td>";
		$ch_make ++;
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">�����Ă��܂��܂����B�B</div>";
#koko 2005/04/17
		$c_mouke = $dameegitame;
		if(!$c_mouke){$c_mouke = 100;}
		print "<div align=center style=\"color:#339933;font-size:14px;\">$c_mouke�~��ɓ��ꂽ�B</div>";
#kokoend
	}else{
		$ch_yobi1 = "<td align=center>$my_chara_para[1] vs $aite_chara_para[1]</td><td align=center>��������</td><td>�[</td>";
		$ch_hikiwake ++;
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">���������܂���ł����B�B���������ł��B</div>";
#koko 2005/04/17
		$c_mouke = int($dameegitame * 1.5);
		if(!$c_mouke){$c_mouke = 100;}
		print "<div align=center style=\"color:#339933;font-size:14px;\">$c_mouke�~��ɓ��ꂽ�B</div>";
#kokoend
	}
	
	$ch_gazou ="$my_chara_para[3]";
	$ch_lasttime = $now_time;
	$c_sinki_temp = "$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_kati<>$ch_make<>$ch_hikiwake<>$ch_yuusyou<>$ch_lasttime<>$ch_yobi1<>$ch_yobi2<>$ch_yobi3<>$ch_yobi4<>$ch_yobi5<>$ch_yobi6<>\n"; 
	unshift (@all_taisen_list,$c_sinki_temp);
	unshift (@all_taisen_list,$league_meisai);
	open(TOO,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	eval{ flock (TOO, 2); };
	print TOO @all_taisen_list;
	close(TOO);
	&unlock;#koko 2005/04/17;�����o�O
#koko 2005/04/17
	$money += $c_mouke;
#�f�[�^�X�V 
	&temp_routin;#&temp_routin;
	&log_kousin($my_log_file,$k_temp);#&log_kousin($my_log_file,$k_temp);
#kokoend
	&hooter("c_league","�߂�","game.cgi");
	exit;
	}		#�����̏ꍇ�̕�

		&header(keiba_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td bgcolor=#ffffff>�ŋ��̃L�����N�^�[�����߂�uC���[�O�v�ł��B$c_nissuu���Ԃ�$c_siaisuu�������s�����Ƃ��ł��܂��B�����Ƃ��������̑����L�����N�^�[���D���ƂȂ�܂��B�����Ԋu��$c_siai_kankaku���ł��B</td>
	<td  bgcolor=#333333 align=center width=200><img src="$img_dir/cleague_tytle.gif"></td>
	</tr></table><br>
		
		<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
		<tr><td>
EOM

	@alldata = (); #koko2007/07/16
	foreach (@aite_erabi){
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
			if ($name eq $ch_oyaname){
				$my_genzaino_joukyou = "$_";		#�����̏󋵂�ϐ��ɓ���Ă���
			}
#koko2005/08/03		$key=(split(/<>/,$_))[4];		#�\�[�g����v�f��I��
#			$key2=(split(/<>/,$_))[11];		#�\�[�g����v�f��I��
#			$key3=(split(/<>/,$_))[10];		#�\�[�g����v�f��I��
			push @alldata,$_;
#			push @keys,$key;
#			push @keys2,$key2;
#			push @keys3,$key3;
	}
	
#		sub bykeys{$keys[$b] <=> $keys[$a];}
#		@junidata=@alldata[ sort bykeys 0..$#alldata]; 
#
		@keys1 = map {(split /<>/)[4]} @alldata;
		@junidata = @alldata[sort {$keys1[$b] <=> $keys1[$a]} 0 .. $#keys1];
#		
#		sub bykeys3{$keys3[$b] <=> $keys3[$a];}
#		@sougoujunidata=@alldata[ sort bykeys3 0..$#alldata]; 
#
		@keys3 = map {(split /<>/)[10]} @alldata;
		@sougoujunidata = @alldata[sort {$keys3[$b] <=> $keys3[$a]} 0 .. $#keys3];
#		
#		sub bykeys2{$keys2[$b] <=> $keys2[$a];}
#		@zenkaijunidata=@alldata[ sort bykeys2 0..$#alldata]; 
#
		@keys2 = map {(split /<>/)[11]} @alldata;
		@zenkaijunidata = @alldata[sort {$keys2[$b] <=> $keys2[$a]} 0 .. $#keys2];
#kokoend

			($zibun_k_id,$zibun_name,$zibun_oyaname,$zibun_gazou,$zibun_kati,$zibun_make,$zibun_hikiwake) = split(/<>/,$my_genzaino_joukyou);
			if ($my_genzaino_joukyou ne ""){
				$syouhai_hyouzi = "�w$zibun_name�x�͌��݁A$zibun_kati��$zibun_make�s$zibun_hikiwake����";
			}
	print <<"EOM";
	<div align=center class=dai>��$nankai_taikai���� - $nannitime���� -</div>
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="c_league">
	<input type=hidden name=command value="game">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value=����������></form>
	$syouhai_hyouzi
	</div>
	<hr size=1>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=3>
	���ŋ߂̎���
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td>�΁@��</td><td nowrap>���@��</td><td nowrap>���߂̃R�����g</td></tr>
EOM

	$i=1;
#	foreach (@alldata) {
	foreach (@aite_erabi) { #koko2005/08/03
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		print "<tr class=sita2>$ch_yobi1</tr>";
				if($i >=5){last;}
			$i++;
	}

	print <<"EOM";
	</table><br><br>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=7>
	�����݂܂ł̏��ʁi�x�X�g10�j
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td></td><td nowrap>���O</td><td>�쐬��</td><td>���@��</td><td nowrap>�s�@��</td><td>��������</td><td>����������</td><td nowrap>�D����</td></tr>
EOM

	$i=1;
	foreach (@junidata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($i <= 3 && $ch_gazou ne ""){$ch_name_hyouzi = "<img src=$ch_gazou $chara_gazou_size><br>$ch_name";}else{$ch_name_hyouzi = "$ch_name";}
		$siaisyouka = $ch_kati + $ch_make + $ch_hikiwake;
		print <<"EOM";
		<tr class=sita2><td align=center>$i</td><td nowrap align=center>$ch_name_hyouzi</td><td align=center>$ch_oyaname</td><td align=right nowrap>$ch_kati��</td><td align=right nowrap>$ch_make�s</td><td align=right>$ch_hikiwake����</td><td align=right nowrap>$siaisyouka</td><td align=right nowrap>$ch_yuusyou��</td></tr>
EOM
				if($i >=10){last;}
			$i++;
	}
	print "</table>";
	
	if ($nankai_taikai != 1){ 
	print <<"EOM";
	<br><br>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=7>
	���O����̏��ʁi�x�X�g5�j
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td></td><td nowrap>���O</td><td>�쐬��</td><td>���@��</td><td nowrap>�s�@��</td><td>��������</td><td nowrap>�D����</td></tr>
EOM

	$i=1;
	foreach (@zenkaijunidata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($i == 1 && $ch_gazou ne ""){$ch_name_hyouzi = "<img src=$ch_gazou $chara_gazou_size><br>$ch_name";}else{$ch_name_hyouzi = "$ch_name";}
		$siaisyouka = $ch_kati + $ch_make + $ch_hikiwake;
		print <<"EOM";
		<tr class=sita2><td align=center>$i</td><td nowrap align=center>$ch_name_hyouzi</td><td align=center>$ch_oyaname</td><td align=right nowrap>$ch_yobi3��</td><td align=right nowrap>$ch_yobi4�s</td><td align=right>$ch_yobi5����</td><td align=right nowrap>$ch_yuusyou��</td></tr>
EOM
				if($i >= 5){last;}
			$i++;
	}
	print "</table>";
	print <<"EOM";
	<br><br>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=7>
	���������ʁi�|�C���g�l���x�X�g10�j<br>
	�D����10�|�C���g�A�Q�ʁ�5�|�C���g�A�R�ʁ�3�|�C���g�A�S�ʁ�2�|�C���g�A�T�ʁ�1�|�C���g�����Z����A���̗ݐσ|�C���g���Ō��肵�܂��B
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td></td><td nowrap>���O</td><td>�쐬��</td><td>�l���|�C���g</td><td nowrap>�D����</td></tr>
EOM

	$i=1;
	foreach (@sougoujunidata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($ch_yobi2 eq ""){next;}
		if ($i <= 3 && $ch_gazou ne ""){$ch_name_hyouzi = "<img src=$ch_gazou $chara_gazou_size><br>$ch_name";}else{$ch_name_hyouzi = "$ch_name";}
		$siaisyouka = $ch_kati + $ch_make + $ch_hikiwake;
		print <<"EOM";
		<tr class=sita2><td align=center>$i</td><td nowrap align=center>$ch_name_hyouzi</td><td align=center>$ch_oyaname</td><td align=right nowrap>$ch_yobi2�|�C���g</td><td align=right nowrap>$ch_yuusyou��</td></tr>
EOM
				if($i >= 10){last;}
			$i++;
	}
	print "</table>";
	
	}		#�P����łȂ��ꍇ�̕�
		&hooter("login_view","�߂�");
		exit;
}

#####C���[�O�ւ̓o�^����
sub c_league_touroku {
	open(TO,"< $doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	eval{ flock (TO, 1); };
	my @touroku_list = <TO>;
	close(TO);	
	my($ch2_k_id,$ch2_name,$ch2_oyaname,$ch2_gazou)= split(/<>/,@_[0]);
	$c_sinki_temp = "$ch2_k_id<>$ch2_name<>$ch2_oyaname<>$ch2_gazou<>0<>0<>0<>0<>$ch2_lasttime<>$ch2_yobi1<>$ch2_yobi2<>$ch2_yobi3<>$ch2_yobi4<>$ch2_yobi5<>$ch2_yobi6<>\n"; 
	push (@touroku_list,$c_sinki_temp);
	open(TOO,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	eval{ flock (TOO, 2); };
	print TOO @touroku_list;
	close(TOO);
	$my_genzaino_joukyou = "$c_sinki_temp";		#�����̏󋵂�ϐ��ɓ���Ă���
}

sub ch_kougeki {
#�U�����e�������_���őI��
		$battle_rand = int(rand(17))+1;
		print "<table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=center><tr align=center><td>";
##�����̍U���̏ꍇ
		if (@_[0] == 1){
			print "<div style=\"color:#339933;font-size:12px;\" align=left>@_[1]�̍U���I<br>";
#�U�����e
			&ch_kougekinaiyou (1,$aite_chara_para[1]);
#���ʕ\��
			if ($damage eq "no_d"){
					print "<div style=\"color:#ff3300;font-size:12px;\" align=right>$return_naiyou</div>\n";
			}else{
					print "<div style=\"color:#339933;font-size:12px;\" align=right>$return_naiyou</div>\n";
					$aite_chara_power -= $damage;
			}
			
##����̍U���̏ꍇ
		}else {
			print "<div style=\"color:#ff3300;font-size:12px;\" align=right>@_[1]�̍U���I<br>";
			&ch_kougekinaiyou (0,$my_chara_para[1]);
#���ʕ\��
#�����ɂ����Ȃ��ꍇ
			if ($damage eq "no_d"){
					print "<div style=\"color:#339933;font-size:12px;\" align=left>$return_naiyou</div>\n";
			}else{
#�_���[�W���󂯂��ꍇ
					print "<div style=\"color:#ff3300;font-size:12px;\" align=left>$return_naiyou</div>\n";
					$my_chara_power -= $damage;
			}
		}
	print "</td></tr></table>";
}

###�U�����e���Ƃ̃_���[�W�����T�u���[�`��
sub ch_kougekinaiyou {
# @_[0]��1�Ȃ玩���̍U���A0�Ȃ瑊��̍U��
	if (@_[0] == 1){$align_settei = "align=left";}else{$align_settei = "align=right";}
	
			$battle_naiyou_hanbetu = $battle_rand + 26;	#�o�g�������_���l�̂P������̃R�����g�ɂȂ�悤�ɂ���
			if ($battle_rand <= 8 || $battle_rand == 15 || $battle_rand == 16){
				$seisinornikutai = "���_�I�_���[�W���󂯂��I";
			}else{$seisinornikutai = "���̓I�_���[�W���󂯂��I";}
			if (@_[0] == 1){
				print "$my_chara_para[$battle_naiyou_hanbetu]</div><br>\n";
			}else{
				print "$aite_chara_para[$battle_naiyou_hanbetu]</div><br>\n";
			}
# iryoku_hantei (�U����,�U���̓��e)
			&ch_iryoku_hantei (@_[0],$battle_rand);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]�̓_���[�W���󂯂Ȃ������B";}
			else{$return_naiyou = "@_[1]�� <span style=\"font-size:18px\">$damage</span> ��$seisinornikutai";}

	if (@_[0] == 1 && $damage ne "no_d"){$dameegitame += $damage;}	#koko 2005/04/17

}

#�З͔���T�u���[�`��
sub ch_iryoku_hantei {
#�U���̓��e���Ƃ̔\�͒l
	$iryoku_hanteiti = @_[1] + 5;		#�o�g�������_���l�̂P������̔\�͂ɂȂ�悤�ɂ���
#koko2007/10/13
	$myrad1 = int(rand(3));
	if($myrad1 == 0){
		$batoru1 = $my_chara_para[$iryoku_hanteiti] - int($my_chara_para[$iryoku_hanteiti] / 3);
	}elsif($myrad1 == 1){
		$batoru1 = $my_chara_para[$iryoku_hanteiti] + int($my_chara_para[$iryoku_hanteiti] / 3);
	}else{
		$batoru1 = $my_chara_para[$iryoku_hanteiti];
	}
	$myrad2 = int(rand(3));
	if($myrad2 == 0){
		$batoru2 = $aite_chara_para[$iryoku_hanteiti] - int($aite_chara_para[$iryoku_hanteiti] / 3);
	}elsif($myrad2 == 1){
		$batoru2 = $aite_chara_para[$iryoku_hanteiti] + int($aite_chara_para[$iryoku_hanteiti] / 3);
	}else{
		$batoru2 = $aite_chara_para[$iryoku_hanteiti];
	}
	if (@_[0] == 1){
		$hantei_kakkati = $batoru1 - $batoru2;
	}else{
		$hantei_kakkati = $batoru2 - $batoru1;
	}
#end2007/10/13
	if ($hantei_kakkati <= 0){
			$damage = "no_d";
	}else{
			$damage = "$hantei_kakkati";
	}
}

###����������
sub taikai_syokika {
			&lock;
	@alldata = (); #koko2007/07/16
	foreach (@aite_erabi){
		my ($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
#koko2005/08/03			$key=(split(/<>/,$_))[4];		#�\�[�g����v�f��I��
			push @alldata,$_;
#			push @keys,$key;
	}
	
#		sub bykeys{$keys[$b] <=> $keys[$a];}
#		@junidata=@alldata[ sort bykeys 0..$#alldata]; 
		@keys0 = map {(split /<>/)[4]} @alldata;
		@junidata = @alldata[sort {$keys0[$b] <=> $keys0[$a]} 0 .. $#keys0];
#kokoend

	$i = 1;
	@new_aite_erabi = (); #koko2007/07/16
	foreach (@junidata){
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		$ch_yobi3 = $ch_kati;
		$ch_yobi4 = $ch_make;
		$ch_yobi5 = $ch_hikiwake;
		$ch_kati = 0;
		$ch_make = 0;
		$ch_hikiwake = 0;
		if ($i == 1){$ch_yuusyou ++; $ch_yobi2 += 10;}
		if ($i == 2){$ch_yobi2 += 5;}
		if ($i == 3){$ch_yobi2 += 3;}
		if ($i == 4){$ch_yobi2 += 2;}
		if ($i == 5){$ch_yobi2 += 1;}
		$c_sinki_temp = "$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_kati<>$ch_make<>$ch_hikiwake<>$ch_yuusyou<>$ch_lasttime<>$ch_yobi1<>$ch_yobi2<>$ch_yobi3<>$ch_yobi4<>$ch_yobi5<>$ch_yobi6<>\n"; 
		push (@new_aite_erabi,$c_sinki_temp);
		$i ++;
	}
			$nankai_taikai ++;
			$league_meisai = "$now_time<>$nankai_taikai<>\n";
			@aite_erabi = @new_aite_erabi;
			@alldata = ();
			$nannitime = 1;
			unshift (@new_aite_erabi,$league_meisai);
			open(OUT,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
			eval{ flock (OUT, 2); };
			print OUT @new_aite_erabi;
			close(OUT);			
			&unlock;
	
}

#######�V�K�o�^����
sub new {
	if ($new_touroku_per == 1) {&error("���݁A�V�K�o�^�𒆎~���Ă��܂��B");}		#ver.1.40
	&lock;
	&get_host;
	if($in{'name'} eq '' || $in{'pass'} eq '' || $in{'sex'} eq ''){&error("�L���R�ꂪ����܂��I");}
	if($in{'name'}  =~ / / || $in{'name'}  =~ /�@/){&error("���O�ɃX�y�[�X���g��Ȃ��ł�������");}
	if($in{'name'}  =~ /,/){&error("���O�Ɂu,�v���g��Ȃ��ł�������");}		#ver.1.3
#ver.1.40��������
	open(IN,"< $logfile") || &error("Open Error : $logfile");
	eval{ flock (IN, 1); };
	@all_sankasya = <IN>;

	foreach (@tazyu_kyoka){if ($in{'name'} eq $_){$kyoka_ok = 1;}} # ���d�o�^���̓`�F�b�N���Ȃ�#koko2006/03/05

	foreach (@all_sankasya) {
		&kozin_sprit;
		if($in{'name'} eq $name){ &error("���̖��O�͂��łɓo�^����Ă��܂��B�ʂ̖��O�ł��������������B");}
		if ($tajuukinsi_flag==1){
			if($return_host eq $host && !$kyoka_ok){ &error("��d�o�^�͋֎~�ł��B");} #koko2006/03/05
		}
	}
	close(IN);
#ver.1.40��������
#koko2007/04/26 �����_���Љ��
#koko2007/10/13
	if($in{'syokai'} eq $in_aikotoba && $in_aikotoba ne ''){
		$my_m_comment = "$in{'name'}���񂪐V�K�o�^����A�V���������o�[�ɂȂ�܂����B";
	}elsif ($syokai eq 'yes' ){
		($in_syoukai_id,$no) = split(/=/, $in{'syokai'});#koko2007/04/22
		if (!$in_syoukai_id){ &error("�Љ�R�[�h������܂���B");}
		if (!$no){&error("�Љ�Ă��ꂽ���肪���܂���B");}
#  �Љ�҂̃t�@�C������������t�@�C�����I�[�v��
		$aite_f = "./member/$no/log.cgi";
		if (! -e $aite_f){&error("�Љ�҂�������܂���B");}
		open (IN,"< $aite_f" || &error("�t�@�C�����J�����Ƃ��o���܂���ł����B"));
		eval{ flock (IN, 1); };
		$aite_tep = <IN>;
		close(IN);
		&aite_sprit($aite_tep);
		if ($aite_syoukai_id ne $in_syoukai_id){&error("�m�荇������R�[�h�𕷂��ēo�^���Ă��������B");}
#koko2007/09/20 �Љ�҂ɏЉ�̐U�荞�݁B
		if ($syoukai_majin eq 'yes'){
			$okane = 100000; # �Љ
		#	&lock;	
			&openAitelog ($no);
			$aite_bank += $okane;
			&aite_temp_routin;
			open(OUT,">$aite_log_file") || &error("$aite_log_file���J���܂���");
			eval{ flock (OUT, 2); };
			print OUT $aite_k_temp;
			close(OUT);
			&aite_kityou_syori("�Љ($in{'name'})","",$okane,$aite_bank,"��",$no,"lock_off");
		#	&unlock;
		}
#kokoend
		$syoukai_ari = 1; #koko2007/10/13
		$my_m_comment = "$in{'name'}���񂪐V�K�o�^����A�V���������o�[�ɂȂ�܂����B$in{'syokai'} $aite_name����̏Љ�ł��B";#koko2007/04/22
		$aite_syoukai_id = "";
	#	�Љ�҂̃t�@�C������������t�@�C�����I�[�v���Љ��̃t�@�C�������������B�����R�[�h���g���Ȃ�����B
		open(OUT,">$aite_f") || &error("$aite_f�ɏ������߂܂���");
		eval{ flock (OUT, 2); };
		&aite_temp_routin;
		print OUT $aite_k_temp;
		close(OUT);
#koko2007/09/13
	}elsif($in{'syokai'} ne $in_aikotoba && $syokai eq ''){
		&error("�m�荇������R�[�h�𕷂��ēo�^���Ă��������B");
	}else{
		$my_m_comment = "$in{'name'}���񂪐V�K�o�^����A�V���������o�[�ɂȂ�܂����B";#koko2006/12/29
	}
#kokoend

#�p�X���[�h���X�g����V�KID���擾
	open(PA,"< $pass_logfile") || &error("Open Error : $pass_logfile");
	eval{ flock (PA, 1); };
	@all_pass_list = <PA>;
	close(PA);
	($saisin_id)= split(/<>/,$all_pass_list[0]);
	$saisin_id ++;

	$para1= 5 + (int(rand(15)));$para2= 5 + (int(rand(15)));$para3= 5 + (int(rand(15)));$para4= 5 + (int(rand(15)));$para5= 5 + (int(rand(15)));$para6= 5 + (int(rand(15)));$para7= 5 + (int(rand(15)));$para8= 5 + (int(rand(15)));$para9= 5 + (int(rand(15)));$para10= 5 + (int(rand(15)));$para11= 5 + (int(rand(15)));$para12= 5 + (int(rand(15)));$para13= 5 + (int(rand(15)));$para14= 5 + (int(rand(15)));$para15= 5 + (int(rand(15)));$para16= 5 + (int(rand(15)));$para17= 5 + (int(rand(15)));
	if($in{'sex'} eq "m"){
			$sintyou= 165 + (int(rand(20)));
	}else{
			$sintyou= 150 + (int(rand(25)));
	}
	if($in{'sex'} eq "m"){
			$taijuu= 50 + (int(rand(35)));
	}else{
			$taijuu= 48 + (int(rand(20)));
	}
	&time_get;
	$last_syokuzi = $date_sec - ($syokuzi_kankaku*60);		#ver.1.3
	if($syoukai_ari){$syoukai_in = 100000;}else{$syoukai_in = 50000;} #koko2007/10/13
	$new_temp="$saisin_id<>$in{'name'}<>$in{'pass'}<>$syoukai_in<>0<>�w��<>$para1<>$para2<>$para3<>$para4<>$para5<>$para6<>$para7<>$para8<>$para9<>$para10<>$para11<>$para12<>$para13<>$para14<>$para15<>$para16<>$para17<>$date_sec<><>$in{'sex'}<>$date_sec<>$date<>$return_host<><><><><><>0<>100<><><>$last_syokuzi<>$sintyou<>$taijuu<>100<><>0<>0<><>50<><><><><>$k_yobi3<>$k_yobi4<>0<><><>\n"; #koko2007/02/11,2007/10/13
	
	$pass_temp = "$saisin_id<>$in{'name'}<>$in{'pass'}<>\n";
	
#�����p�f�B���N�g�������O�t�@�C���쐬
	$my_directry = "./member/$saisin_id";
	$my_log_file = "$my_directry/log.cgi";
	mkdir($my_directry, 0755) || &error("ID�ԍ�$saisin_id�̃f�B���N�g�������ɑ��݂��Ă��܂��B");
	if ($zidouseisei == 1){
		chmod 0777,"$my_directry";
	}elsif ($zidouseisei == 2){
		chmod 0755,"$my_directry";
	}else{
		chmod 0755,"$my_directry";
	}
	open(MYF,">$my_log_file") || &error("Open Error : $my_log_file");
	eval{ flock (MYF, 2); };
	print MYF $new_temp;
	chmod 0666,"$my_log_file";
	close(MYF);
#���b�Z�[�W�����p�t�@�C���쐬
	$message_file="$my_directry/mail.cgi";
	open(MF,">$message_file") || &error("Write Error : $message_file");
	eval{ flock (MF, 2); };
	chmod 0666,"$message_file";
	close(MF);
#koko2006/12/23�@�擪�ɒ�`�ς�
#	$kanrisya_id = "1";
#	$kanrisyaname = '�q�������[';
#	$m_comment = '�Ǘ��l������Ă��܂��B<br>�n�߂͓������o�C�g����n�߂Ă��������ˁB<br>�s���l�܂����菕���̗~�����Ƃ��͉��������ǂ����B<br>��낵�����肢���܂��B';
#koko2007/11/07 ����悪�������̏���
	if($kanrisyaname ne ''){
		open(AIT,"< $message_file") || &error("������̕��̃��[���L�^�t�@�C���i$message_file�j���J���܂���B");
		eval{ flock (AIT, 1); };
		$last_mail_check_time = <AIT>;
		@mail_cont = <AIT>;
		close(AIT);

		&time_get;
		$new_mail = "��M<>$kanrisyaname<>$m_comment<>$date2<>$date_sec<><><><><><>\n";
		unshift (@mail_cont,$new_mail);
		if (@mail_cont > $mail_hozon_gandosuu){pop @mail_cont;}	#ver.1.30
#�ŏI���[���`�F�b�N���Ԃ��Ȃ���΂P������
		if ($last_mail_check_time eq ""){$last_mail_check_time = "1\n";}
		unshift (@mail_cont,$last_mail_check_time);
#	&lock; #koko2006/10/18
		open(OUT,">$message_file") || &error("$message_file�ɏ������߂܂���");
		eval{ flock (OUT, 2); };
		print OUT @mail_cont;
		close(OUT);
#	&unlock; #koko2006/10/18

#�����̃��[���ɂ����M�ς݃��b�Z�[�W�Ƃ��ċL�^�i�Ǘ��҃��[���łȂ���΁j
		$my_sousin_file="./member/$kanrisya_id/mail.cgi";
		if (-e "$my_sousin_file"){ #�Ǘ��҂��Ȃ������M�����B$koko2006/12/31
			open(ZIB,"< $my_sousin_file") || &error("$my_sousin_file���J���܂���B");
			eval{ flock (ZIB, 1); };
			$my_last_mail_check_time = <ZIB>;
			@my_mail_cont = <ZIB>;
			close(ZIB);
#$my_m_comment;
			$sousin_mail = "��M<>$in{'name'}<>$my_m_comment<>$date2<>$date_sec<><><><><><>\n";
			unshift (@my_mail_cont,$sousin_mail);
			if (@my_mail_cont > $mail_hozon_gandosuu){pop @my_mail_cont;}#ver.1.30
#�ŏI���[���`�F�b�N���Ԃ��Ȃ���΍��̎��Ԃ�����
			if ($my_last_mail_check_time eq ""){$my_last_mail_check_time = "$date_sec\n";}
			unshift (@my_mail_cont,$my_last_mail_check_time);
#		&lock; #koko2006/10/18
			open(ZIBO,">$my_sousin_file") || &error("$my_sousin_file�ɏ������߂܂���");
			eval{ flock (ZIBO, 2); };
			print ZIBO @my_mail_cont;
			close(ZIBO);
#		&unlock; #koko2006/10/18
		}
	}
#kokoend
	
#�w�����L�^�t�@�C���쐬
	$monokiroku_file="$my_directry/mono.cgi";
	open(MK,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
	eval{ flock (MK, 2); };
	chmod 0666,"$monokiroku_file";
	close(MK);
	
#��s���׋L�^�t�@�C���쐬
	$ginkoumeisai_file="$my_directry/ginkoumeisai.cgi";
	open(GM,">$ginkoumeisai_file") || &error("Write Error : $ginkoumeisai_file");
	eval{ flock (GM, 2); };
	chmod 0666,"$ginkoumeisai_file";
	close(GM);

#���X�g�p���O�t�@�C���쐬
	push (@all_sankasya,$new_temp);
	if ($mem_lock_num == 0){
		$err = &data_save($logfile, @all_sankasya); #koko2007/07/07
		if ($err) {&error("$err");}
	}else{
		open(OUT,">>$logfile") || &error("Write Error : $logfile");
		eval{ flock (OUT, 2); };
		print OUT $new_temp;
		close(OUT);
	}
#�p�X���[�h�L�^�t�@�C���X�V
	unshift (@all_pass_list,$pass_temp);
		open(PAO,">$pass_logfile") || &error("Write Error : $pass_logfile");
		eval{ flock (PAO, 2); };
		print PAO @all_pass_list;
		close(PAO);
#ver.1.40�����܂�

#�j���[�X�L�^
	&news_kiroku("����","$in{'name'}���񂪐V�����Z���ɂȂ�܂����B");		#ver.1.3

	&unlock;
	&set_cookie;
	&header;
	&check_pass;
	print <<"EOM";
	<div align=center>
	<br><br>�ȉ��̓��e�ŏZ���o�^���������܂����B<br><br>
	
<table width="450" border="0" cellspacing="0" cellpadding="4" align=center style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px" bgcolor=$st_win_back>
<tr>
<td  width="25%"><span class=honbun2>���O</span>�F$name</td>
<td><span class=honbun2>�p�X</span>�F$pass</td>
<td width="25%"><span class=honbun2>�g��</span>�F$sintyou</td>
<td width="25%"><span class=honbun2>�̏d</span>�F$taijuu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  width="25%"><span class=tyuu>�����]</span></td>
<td><span class=honbun2>����</span>�F$kokugo</td>
<td width="25%"><span class=honbun2>���w</span>�F$suugaku</td>
<td width="25%"><span class=honbun2>����</span>�F$rika</td></tr>
<tr><td width="25%"><span class=honbun2>�Љ�</span>�F$syakai</td>
<td width="25%"><span class=honbun2>�p��</span>�F$eigo</td>
<td width="25%"><span class=honbun2>���y</span>�F$ongaku</td>
<td width="25%"><span class=honbun2>���p</span>�F$bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px"><td  width="25%"><span class=tyuu>���g��</span></td>
<td><span class=honbun2>���b�N�X</span>�F$looks</td>
<td><span class=honbun2>�̗�</span>�F$tairyoku</td>
<td><span class=honbun2>���N</span>�F$kenkou</td></tr>
<tr><td><span class=honbun2>�X�s�[�h</span>�F$speed</td>
<td><span class=honbun2>�p���[</span>�F$power</td>
<td><span class=honbun2>�r��</span>�F$wanryoku</td>
<td><span class=honbun2>�r��</span>�F$kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px"><td  width="25%"><span class=tyuu>�����̑�</span></td>
<td><span class=honbun2>LOVE</span>�F$love</td>
<td><span class=honbun2>�ʔ���</span>�F$unique</td>
<td><span class=honbun2>�G�b�`</span>�F$etti</td></tr>
</table>
	
		<br><br><a href=$script>�߂�</a>
	</div>
	</body></html>
EOM
exit;
}

######�f�[�^�ۑ�
sub data_hozon {		#ver.1.40
	&lock;
	open(DH,"< $logfile") || &error("Open Error : $logfile");
	eval{ flock (DH, 1); };
		@ranking_data = <DH>;
	close(DH);
	$sonzai_flag=0;
	$i = 0;
	foreach (@ranking_data){
		&list_sprit($_);
		if ($k_id eq "$list_k_id"){
			$ranking_data[$i] = $my_prof;
			$sonzai_flag = 1;
			last;
		}
		$i ++;
#		&list_temp;
#		push (@new_ranking_data,$list_temp);
	}
	if ($sonzai_flag==0){unshift (@ranking_data,$my_prof);}
#	unshift (@new_ranking_data,$my_prof);
	
#�iver.1.40��������j
	if ($mem_lock_num == 0){
		$err = &data_save($logfile, @ranking_data);#koko2007/07/07
		if ($err) {&error("$err");}
	}else{
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		eval{ flock (OUT, 2); };
		print OUT @ranking_data;
		close(OUT);
	}
#�iver.1.40�����܂Łj
#�t�H���_�[���̃t�@�C�������擾���ăo�b�N�A�b�v���O���쐬
					use DirHandle;
					$dir = new DirHandle ("./member/"."$k_id");
#ver.1.2�R�R����
					$back_folder_name = "$k_id" . "backup";
					$back_folder_pass = "./member/$back_folder_name";
					if (! -e "./member/$back_folder_name"){
						mkdir($back_folder_pass, 0755) || &error("Error : can not Make Directry");
							if ($zidouseisei == 1){
								chmod 0777,"$back_folder_pass";
							}elsif ($zidouseisei == 2){
								chmod 0755,"$back_folder_pass";
							}else{
								chmod 0755,"$back_folder_pass";
							}
					}
#ver.1.2�R�R�܂�
					while($file_name = $dir->read){ #1�ǂݍ����$folder_name�ɑ��
							if($file_name eq '.' || $file_name eq '..' || $file_name =~ /^backup_/ || $file_name eq '.DS_Store'){next;}
							$backup_name = "backup_" ."$file_name";
							open (BK,"< ./member/$k_id/$file_name")  || &error("Open Error : ./member/$k_id/$file_name");
							eval{ flock (BK, 1); };
							@back_data = <BK>;
							close (BK);
							if (@back_data != ""){		#ver.1.22
								open (BKO,">./member/$back_folder_name/$backup_name");		#ver.1.2
								eval{ flock (BKO, 2); };
								print BKO @back_data;
								close (BKO);
							}				#ver.1.22
					}
					$dir->close;  #�f�B���N�g�������
#ver.1.30��������
	open(GUEST,"< $guestfile");
	eval{ flock (GUEST, 1); };
	@all_guest=<GUEST>;
	close(GUEST);
	@new_all_guest = ();
	foreach (@all_guest) {
		($sanka_timer,$sanka_name,$hyouzi_check) = split(/<>/);
		if ($name eq "$sanka_name"){next;}
		$sanka_tmp = "$sanka_timer<>$sanka_name<>$hyouzi_check<>\n";
		push (@new_all_guest,$sanka_tmp);
	}
#ver.1.40��������
	if ($mem_lock_num == 0){
		$err = &data_save($guestfile, @new_all_guest);#koko2007/07/07
		if ($err) {&error("$err");}
	}else{
		open(GUEST,">$guestfile");
		eval{ flock (GUEST, 2); };
		print GUEST @new_all_guest;
		close(GUEST);
	}
#ver.1.40�����܂�
#ver.1.30�����܂�
	&unlock;
	&set_cookie;
	&header("","sonomati");
	my ($date_sec) = time;
	$tabetenaizikan = $date_sec - $last_syokuzi ;
	$manpuku_time = $syokuzi_kankaku*60;
	if ($job eq "�w��" && $tabetenaizikan > $manpuku_time + 60*60*24*($deleteUser - 10)){
		$logout_keikoku_mes1 = "<font color=red>���ӁI�E�ƂɏA���Ă��Ȃ����߁A<BR>���̂܂܂ł̓f�[�^�폜����Ă��܂��܂��B<BR>�X�̒��́uWORK�v�ŏA�E��\��\�\\�ł��B<BR>�܂��A���ɐE�ƂɏA�����Ƃ��Ă�<BR>�����ԐH�����Ƃ��Ă��Ȃ����߁A<BR>���̂܂܂ł̓f�[�^�폜����Ă��܂��܂��B<BR>�X�̒��́uFOOD�v�ŐH����\��\�\\�ł��B</font>";
	}elsif ($tabetenaizikan > $manpuku_time + 60*60*24*($deleteUser - 10)){
		$logout_keikoku_mes1 = "<font color=red>���ӁI�����ԐH�����Ƃ��Ă��Ȃ����߁A<BR>���̂܂܂ł̓f�[�^�폜����Ă��܂��܂��B<BR>�X�̒��́uFOOD�v�ŐH����\��\�\\�ł��B</font>";
		}elsif ($job eq "�w��"){
		$logout_keikoku_mes1 = "<font color=red>���ӁI�E�ƂɏA���Ă��Ȃ����߁A<BR>���̂܂܂ł̓f�[�^�폜����Ă��܂��܂��B<BR>�X�̒��́uWORK�v�ŏA�E��\��\�\\�ł��B</font>";
	}else{$logout_keikoku_mes1 = "�܂��̂����p�����҂����Ă���܂��B";
		}
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
���݂̏�Ԃ�ۑ����܂����B<BR>
����ꂳ�܂ł����B<BR>
�I���̍ۂ́A��ʉ��́u���O�A�E�g�v����ǂ����B<BR>
$logout_keikoku_mes1<BR>
<BR>
�Ǘ��l����@�Ȃ�тɁ@�f�P�O�|Project�ꓯ
</span>
</td></tr></table>
<br>
EOM
	&hooter("login_view","�Q�[���ɖ߂�");
	print <<"EOM";
	<div align=center><form method=POST action="$script">
	<input type=submit value="���O�A�E�g">
	</form></div>
EOM
	exit;
}