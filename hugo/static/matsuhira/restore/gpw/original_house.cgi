#!/usr/local/bin/perl

# �����g���̃T�[�o�[�̃p�X�ɍ��킹�Ă��������B
################�@koko 2005/05/05
# �l�ł̂P���̂����K�󂯎����
$osaisenjyougen = 20000;
# �g�[�^���ł̂P���̂����K�󂯎����
$totalosaisenjyougen = 100000;
#
#�����K���������� koko2005/09/01

# �����N�̃{�^����t����('yes','no')
$linkbotan = 'no';

# �Ƃ𔄋p�̎��^�c��Ђ������Ă��܂��B ('yes','no') koko2007/06/17
$baikyku_syoumetu = 'no';

# ����̉Ǝg���i���o�[(0����n�܂�) %ie_hash2
$tokusyu_ie_no = '';
# eval{ flock (IN, 2); }; ���b�N�����@2007/06/17

# �񌬖ڈȌ�̉Ƃ̔{�� #koko2007/08/15
$ie_bairitu = 2;

################ kokoend

$this_script = 'original_house.cgi';
require './jcode.pl';
require './cgi-lib.pl';
require './town_ini.cgi';
require './town_lib.pl';

#require './unei.pl'; #koko2007/04/20�@�g�p���Ă��Ȃ��B
require './unei_2.pl'; #koko2007/04/30�@�ꏊ�ړ�
require './kaishiya.pl'; #koko2007/05/05 �ꏊ�ړ�
require './motimono_hanbai.pl'; #koko2007/09/08
# require './lial_kaishiya.pl'; #koko2007/08/18

&decode;
#�����e�`�F�b�N
	if($mente_flag == 1 && $in{'admin_pass'} eq "" && $in{'mode'} ne ""){&error("$mente_message")}
	
$seigenyou_now_time = time;
#�������ԃ`�F�b�N
		$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $access_byou);
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("�܂��s���ł��܂���B����$ato_nanbyou�b���҂����������B")}
		
#��������
	if($in{'mode'} eq "my_house_settei"){&my_house_settei;}
	elsif($in{'mode'} eq "my_house_settei_do"){&my_house_settei_do;}
	elsif($in{'mode'} eq "houmon"){&houmon;}
	elsif($in{'mode'} eq "bbs1_settei_do"){&bbs1_settei_do;}
	elsif($in{'mode'} eq "omise_settei_do"){&omise_settei_do;}
	elsif($in{'mode'} eq "dokuzi_settei_do"){&dokuzi_settei_do;}
	elsif($in{'mode'} eq "gentei_settei_do"){&gentei_settei_do;}
	elsif($in{'mode'} eq "bbs_regist"){&bbs_regist;}
	elsif($in{'mode'} eq "gentei_delete"){&gentei_delete;}
	elsif($in{'mode'} eq "bbs_delete"){&bbs_delete;}
	elsif($in{'mode'} eq "gentei_regist"){&gentei_regist;}
	elsif($in{'mode'} eq "saisensuru"){&saisensuru;}
	elsif($in{'mode'} eq "comment_change"){&comment_change;}
	elsif($in{'mode'} eq "normal_bbs"){&normal_bbs;}
	elsif($in{'mode'} eq "house_change"){&house_change;}
	elsif($in{'mode'} eq "house_change2"){&house_change2;} #koko2007/08/15
	elsif($in{'mode'} eq "my_syouhin"){&my_syouhin;}
	elsif($in{'mode'} eq "kaisya_bbs_do"){&kaisya_bbs_do;} #koko2007/05/07
	elsif($in{'mode'} eq "seizou"){&seizou;} #koko2007/06/02

	else{&error("�u�߂�v�{�^���ŊX�ɖ߂��Ă�������");}
exit;
	
#############�ȉ��T�u���[�`��

####�����̉Ƃ̐ݒ�
sub my_house_settei {		#ver.1.3
	open(IN,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
	eval{ flock (IN, 1); };
	@ori_ie_para = <IN>;
	close(IN);
	$oriie_atta=0;
	foreach (@ori_ie_para){
		&ori_ie_sprit($_);
		if ($in{'iesettei_id'} eq "$ori_k_id"){
			$oriie_atta=1;
			last;
		}
	}
	if ($oriie_atta == 0){&error("�Ƃ�������܂���B");}
	$my_directry = "./member/$in{'iesettei_id'}";
	$oriie_settei_file="$my_directry/oriie_settei.cgi";
#�Ɛݒ�t�@�C�����Ȃ���΍쐬
	if (! -e $oriie_settei_file){
		open(OIS,">$oriie_settei_file") || &error("Write Error : $oriie_settei_file");
		eval{ flock (OIS, 2); };
		chmod 0666,"$oriie_settei_file";
		close(OIS);
	}
	open(OIS,"< $oriie_settei_file") || &error("Open Error : $oriie_settei_file");
	eval{ flock (OIS, 1); };
	$kihon_oriie_settei = <OIS>;
	&oriie_settei_sprit ($kihon_oriie_settei);
	close(OIS);
	
	&header(kentiku_style);
	if ($in{'iesettei_id'} eq "$k_id"){$settei_title = "�����̉Ɛݒ�"; $settei_t_color = "#336699";}
	else{$settei_title = "�z��҂̉Ɛݒ�"; $settei_t_color = "#ff6666";}
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr bgcolor=$settei_t_color><td align=center style="color:#ffffff;font-size:13px;">$settei_title</td></tr></table><br>
EOM
	if ($my_con1 eq "0"){&bbs1_settei;}elsif ($my_con1 eq "1"){&omise_settei;}elsif ($my_con1 eq "2"){&dokuzi_settei;}elsif ($my_con1 eq "3"){&gentei_settei;}
	if ($my_con2 eq "0"){&bbs1_settei;}elsif ($my_con2 eq "1"){&omise_settei;}elsif ($my_con2 eq "2"){&dokuzi_settei;}elsif ($my_con2 eq "3"){&gentei_settei;}	
	if ($my_con3 eq "0"){&bbs1_settei;}elsif ($my_con3 eq "1"){&omise_settei;}elsif ($my_con3 eq "2"){&dokuzi_settei;}elsif ($my_con3 eq "3"){&gentei_settei;}	
	if ($my_con4 eq "0"){&bbs1_settei;}elsif ($my_con4 eq "1"){&omise_settei;}elsif ($my_con4 eq "2"){&dokuzi_settei;}elsif ($my_con4 eq "3"){&gentei_settei;}
	
#�X�������Ă��Ȃ����@#koko2007/03/22
	if(!($my_con1 eq "1" || $my_con2 eq "1" || $my_con3 eq "1" || $my_con4 eq "1")){ #koko2007/03/23�C��
		@new_ori_ie_list1 = (); #koko2007/07/11
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($in{'iesettei_id'} eq $ori_k_id){		#ver.1.3
				$ori_ie_syubetu = '�X����';
			}
			&ori_ie_temp;
			push (@new_ori_ie_list1,$ori_ie_temp);#koko2007/03/23
		}
#�ƃ��X�g�X�V
#koko2007/09/15
		$i=0;
		$nijyuu = 0;
		foreach (@new_ori_ie_list1){
			if ($_ eq $new_ori_ie_list1[0] && $i){
				$nijyuu = $i;
				&error("��d�������� o_h 1");
				last;
			}
			$i++;
		}
		if ($nijyuu){
			splice @new_ori_ie_list1,$nijyuu;
		}
#kokoend

		open(OIO,">$ori_ie_list") || &error("$ori_ie_list�ɏ������߂܂���");
		eval{ flock (OIO, 2); };
		print OIO @new_ori_ie_list1;#koko2007/03/23
		close(OIO);
	}
#koko2007/08/01
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<div class=tyuu>����{�ݒ�</div>
	���X�ŉƂɃ}�E�X���̂������ɕ\\�������R�����g�i40���ȓ��j<br>
EOM

	$dispin = "";
	$my_iesettei_id = $in{'iesettei_id'};
	foreach (@ori_ie_para){
		&ori_ie_sprit($_);
		($my_iesettei_id,$bangou) = split(/_/,$my_iesettei_id);
		($ori_k_id2,$bangou2) = split(/_/,$ori_k_id);
		if ($my_iesettei_id eq "$ori_k_id2"){
	print <<"EOM";
	<form method=\"POST\" action="$this_script" style="margin-top:0;margin-bottom:0;">
	<input type=hidden name=mode value="comment_change">
	<input type=hidden name=iesettei_id value="$ori_k_id">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=text name=ori_ie_setumei size=80 value=$ori_ie_setumei><input type=submit value="OK"></form>
EOM

		}
	}

	print <<"EOM";
	<hr size=1><!-- kokoend2007/08/01 -->
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="my_house_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	���R���e���c�I���i���ݒu����R���e���c��I�����Ă��������B��ŕύX���\\�ł��B�����̃^�C�g���̓y�[�W��̃{�^���ɕ\\����������̂ł��j<br>
EOM
	if ($ori_ie_rank2 != 3){print "�����ň�ԏ�ɂ���R���e���c���Ƃɓ������Ƃ��ŏ��ɕ\\������܂��B<br>";}

	if ($ori_ie_rank2 == 0){$ii=4;}elsif($ori_ie_rank2 == 1){$ii=3;}elsif($ori_ie_rank2 == 2){$ii=2;}elsif($ori_ie_rank2 == 3){$ii=1;}
		
	$selectcount = 0;
	$titlecount = 4;
	foreach (1..$ii){
		if ($ori_ie_rank2 != 3){print "<div class=honbun2>��$_�߂̃R���e���c</div>";}
		print <<"EOM";
		<select name="�R���e���c$_">
		<option value="">���J���Ȃ�</option>
EOM
		print "<option value=0";
		if ($oriie_settei_sprit[$selectcount] eq "0"){print " selected";}
		print ">�ʏ�̌f����</option>\n";
		print "<option value=1";
		if ($oriie_settei_sprit[$selectcount] eq "1"){print " selected";}
		print ">���X</option>\n";
		print "<option value=2";
		if ($oriie_settei_sprit[$selectcount] eq "2"){print " selected";}
		print ">�Ǝ�URL</option>\n";
		print "<option value=3";
		if ($oriie_settei_sprit[$selectcount] eq "3"){print " selected";}
		print ">�Ǝ�̂ݏ�����f����</option>\n";
		print "</select>\n";

		if ($ori_ie_rank2 != 3) {print "�^�C�g�� <input type=text name=\"�^�C�g��$_\" value=\"$oriie_settei_sprit[$titlecount]\">";}
			$selectcount ++;
			$titlecount ++;
		}
#koko2007/08/15
		print <<"EOM";
		<input type=submit value=OK>
EOM

		print <<"EOM";
	</form>
	<hr size=1>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	���Ƃ̊O�ρA�����i�R���e���c���e�j�̕ύX<br>
	�ꏊ�͂��̂܂܂ɁA�Ƃ̊O�ς�ύX������A�������A�b�v�O���[�h���邱�Ƃ��ł��܂��B<br>
	<input type=submit value=" �I����ʂ� "></form>
EOM
		$ieari_f = '';
		$ie_suu = "$in{'iesettei_id'}"."_0";
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($ie_suu eq $ori_k_id){		#ver.1.3
				$ieari_f = 1;
				last;
			}
		}
		if($ieari_f){
			print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change2">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
<input type=hidden name=iesuu value="0">
	
	�ꏊ�͂��̂܂܁A��1�̊O�ς�ύX
	<input type=submit value=" �I����ʂ�1"></form>
EOM
		}
		$ieari_f = '';
		$ie_suu = "$in{'iesettei_id'}"."_1";
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($ie_suu eq $ori_k_id){		#ver.1.3
				$ieari_f = 1;
				last;
			}
		}
		if($ieari_f){
			print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change2">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
<input type=hidden name=iesuu value="1">
	
	�ꏊ�͂��̂܂܁A��2�̊O�ς�ύX
	<input type=submit value=" �I����ʂ�2"></form>
EOM
		}
		$ieari_f = '';
		$ie_suu = "$in{'iesettei_id'}"."_2";
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($ie_suu eq $ori_k_id){		#ver.1.3
				$ieari_f = 1;
				last;
			}
		}
		if($ieari_f){
			print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change2">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
<input type=hidden name=iesuu value="2">
	
	�ꏊ�͂��̂܂܁A��3�̊O�ς�ύX
	<input type=submit value=" �I����ʂ�3"></form>
EOM
		}
		$ieari_f = '';
		$ie_suu = "$in{'iesettei_id'}"."_3";
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($ie_suu eq $ori_k_id){		#ver.1.3
				$ieari_f = 1;
				last;
			}
		}
		if($ieari_f){
			print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change2">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
<input type=hidden name=iesuu value="3">
	
	�ꏊ�͂��̂܂܁A�Ƃ̊O�ς�ύX
	<input type=submit value=" �I����ʂ�4"></form>
EOM
		}
		print "<hr size=1>";
#kokoend
	if ($in{'iesettei_id'} eq "$k_id"){
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change">
	<input type=hidden name=command value="baikyaku">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	���Ƃ̔��p<br>
	�Ƃ̏ꏊ��ύX�������ꍇ�́A��x�Ƃ𔄋p���Ă���ēx�w�����Ă������B���p�œ�����͓̂y�n�̉��i�����ł��B���݂̃R���e���c���e�͐V���ɉƂ��w�������ꍇ���ێ�����Ă��܂��B<br>
	<input type=submit value=" �Ƃ̔��p "></form>
		
		<div align=center><a href="javascript:history.back()"> [�O�̉�ʂɖ߂�] </a></div>
		</td></tr></table>
EOM
	}else{
		print "���z��҂̉Ƃ̏ꍇ�A���p�����͂ł��܂���B";
	}
		&hooter("login_view","�߂�");
	exit;
}

###�R�����g�ύX
sub comment_change {
	if (length($in{'ori_ie_setumei'}) > 100) {&error("�R�����g��50���ȓ��ł�");}
	if ($in{'ori_ie_setumei'} =~ /'/) {&error("���p�́u'�v�͎g�p�ł��܂���B");}		#ver.1.3
	&lock;
	open(IN,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
	eval{ flock (IN, 1); };
	@ori_ie_para = <IN>;
	close(IN);
	@new_ori_ie_para2 = (); #koko2007/07/11
	foreach (@ori_ie_para){
		&ori_ie_sprit($_);
		if ($in{'iesettei_id'} eq $ori_k_id){
			$ori_ie_setumei = $in{'ori_ie_setumei'};
		}
		&ori_ie_temp;
		push (@new_ori_ie_para2,$ori_ie_temp);#koko2007/03/23
	}

#koko2007/09/15
		$i=0;
		$nijyuu = 0;
		foreach (@new_ori_ie_para2){
			if ($_ eq $new_ori_ie_para2[0] && $i){
				$nijyuu = $i;
				&error("��d�������� o_h 2");
				last;
			}
			$i++;
		}
		if ($nijyuu){
			splice @new_ori_ie_para2,$nijyuu;
		}
#kokoend

	open(OLOUT,">$ori_ie_list") || &error("$ori_ie_list�ɏ������݂��o���܂���");
	eval{ flock (OLOUT, 2); };
	print OLOUT @new_ori_ie_para2;#koko2007/03/23
	close(OLOUT);
	&unlock;
	&message("�Ƃ̃R�����g��ύX���܂����B","my_house_settei","original_house.cgi");
}


###�����̉Ƃ̐ݒ菈��
sub my_house_settei_do {
	$my_directry = "./member/$in{'iesettei_id'}";
	$oriie_settei_file="$my_directry/oriie_settei.cgi";
		open(OIS,"< $oriie_settei_file") || &error("Open Error : $oriie_settei_file");
		eval{ flock (OIS, 1); };
		$kihon_oriie_settei = <OIS>;
		&oriie_settei_sprit ($kihon_oriie_settei);
		close(OIS);
		
		$my_con1 = $in{'�R���e���c1'};
		$my_con2 = $in{'�R���e���c2'};
		$my_con3 = $in{'�R���e���c3'};
		$my_con4 = $in{'�R���e���c4'};
		$my_con1_title = $in{'�^�C�g��1'};
		$my_con2_title = $in{'�^�C�g��2'};
		$my_con3_title = $in{'�^�C�g��3'};
		$my_con4_title = $in{'�^�C�g��4'};
		$my_yobi5 = $in{'my_yobi5'};
		$my_yobi6 = $in{'my_yobi6'};
		$my_yobi7 = $in{'my_yobi7'};
		&oriie_settei_temp;
	&lock;
	open(OLOUT,">$oriie_settei_file") || &error("$oriie_settei_file�ɏ������݂��o���܂���");
	eval{ flock (OLOUT, 2); };
	print OLOUT $ori_ie_settei_temp;
	close(OLOUT);
	&unlock;
	&my_house_settei;
}

####BBS1�̐ݒ�
sub bbs1_settei {
#�Ǘ��ҍ쐬BBS�̏ꍇ
	if ($in{'mode'} eq "admin_bbs"){
			$my_directry = "./member/admin";
			if (! -d $my_directry){
						mkdir($my_directry, 0755) || &error("Error : can not Make Directry");
					if ($zidouseisei == 1){
						chmod 0777,"$my_directry";
					}elsif ($zidouseisei == 2){
						chmod 0755,"$my_directry";
					}else{
						chmod 0755,"$my_directry";
					}
			}
			$bbs1_settei_file="$my_directry/bbs".$in{'bbs_num'}."_ini.cgi";
			if (! -e $bbs1_settei_file){
				open(OIB,">$bbs1_settei_file") || &error("Write Error : $bbs1_settei_file");
				eval{ flock (OIB, 2); };
				chmod 0666,"$bbs1_settei_file";
				close(OIB);
			}
			$bbs1_log_file="$my_directry/bbs".$in{'bbs_num'}."_log.cgi";
			if (! -e $bbs1_log_file){
				open(OIL,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
				eval{ flock (OIL, 2); };
				chmod 0666,"$bbs1_log_file";
				close(OIL);
			}
	}else{
			$my_directry = "./member/$in{'iesettei_id'}";
			$bbs1_settei_file="$my_directry/bbs1_ini.cgi";
			if (! -e $bbs1_settei_file){
				open(OIB,">$bbs1_settei_file") || &error("Write Error : $bbs1_settei_file");
				eval{ flock (OIB, 2); };
				chmod 0666,"$bbs1_settei_file";
				close(OIB);
			}
			$bbs1_log_file="$my_directry/bbs1_log.cgi";
			if (! -e $bbs1_log_file){
				open(OIL,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
				eval{ flock (OIL, 2); };
				chmod 0666,"$bbs1_log_file";
				close(OIL);
			}
	}
		open(OIB,"< $bbs1_settei_file") || &error("Open Error : $bbs1_settei_file");
		eval{ flock (OIB, 1); };
			$bbs1_settei_data = <OIB>;
			($bbs1_title,$bbs1_come,$bbs1_body_style,$bbs1_toukousya_style,$bbs1_table2_style,$bbs1_toukouwidth,$bbs1_a_hover_style,$bbs1_tablewidth,$bbs1_title_style,$bbs1_leed_style,$bbs1_siasenbako,$bbs1_yobi5,$bbs1_yobi6,$bbs1_yobi7,$bbs1_yobi8,$bbs1_yobi9,$bbs1_yobi10,$bbs_link)= split(/<>/,$bbs1_settei_data); #koko2007/06/26
	chomp $bbs_link; #koko2007/06/26
#bbs1_yobi5 = �L���ԍ��̃X�^�C���@bbs1_yobi6�������X�̏Z����p�f���@bbs1_yobi7��input�̃X�^�C��
		close(OIB);
		
#�X�^�C���̏�����
	if ($bbs1_body_style eq ""){$bbs1_body_style = "background-color:#ffcc66;";$syokika = 1;} #koko2007/03/21
	if ($bbs1_title_style eq ""){$bbs1_title_style = "font-size: 16px; color: #666666;line-height:180%; text-align:center;";}
	if ($bbs1_leed_style eq ""){$bbs1_leed_style = "font-size: 11px; line-height: 16px; color: #336699";}
	if ($bbs1_yobi5 eq ""){$bbs1_yobi5 = "font-size: 15px; color: #336699";}
	if ($bbs1_toukousya_style eq ""){$bbs1_toukousya_style = "font-size: 11px; color: #ff6600";}
	if ($bbs1_table2_style eq ""){$bbs1_table2_style = "font-size: 11px; line-height: 16px; color: #666666; background-color:#ffffcc; border: #336699; border-style: dotted; border-width:4px";}
	if ($bbs1_toukouwidth eq ""){$bbs1_toukouwidth = "50";}
	if ($bbs1_a_hover_style eq ""){$bbs1_a_hover_style = " color:#333333;text-decoration: none";}
	if ($bbs1_tablewidth eq ""){$bbs1_tablewidth = "500";}
	if ($bbs1_siasenbako eq ""){$bbs1_siasenbako = "font-size:11px;color:#000000";}
	if ($bbs1_yobi7 eq ""){$bbs1_yobi7 = "font-size:11px;color:#000000";}

	if ($bbs_link){$bbs_link_check = " checked";}

	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="bbs1_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
EOM
	if ($in{'mode'} eq "admin_bbs"){
	print "<input type=hidden name=bbs_num value=\"$in{'bbs_num'}\">\n";
	print "<input type=hidden name=command value=\"admin_bbs\">\n";
	}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
EOM
	if ($in{'mode'} eq "admin_bbs"){
		print "<div class=tyuu>��$admin_bbs_syurui[$in{'bbs_num'}]�̌f���ݒ�</div>";
	}else{
		print "<div class=tyuu>���ʏ�̌f���ݒ�</div>";
	}
	print <<"EOM";
	���f���̃^�C�g���i�^�O�w��B���URL�Ȃ�΃C���[�W�摜�̎w����j<br>
	<textarea  cols=80 rows=4 name="�^�C�g��" wrap="soft">$bbs1_title</textarea><br>
	���^�C�g�����̃R�����g<br>
	<input type=text name="�R�����g" size=120  value=$bbs1_come><br>
	���w�i�̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_body_style" size=120 value="$bbs1_body_style"><br>
	���^�C�g���̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_title_style" size=120 value="$bbs1_title_style"><br>
	���^�C�g�����̃R�����g�̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_leed_style" size=120 value="$bbs1_leed_style"><br>
	���L���ԍ��̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_yobi5" size=120 value="$bbs1_yobi5"><br>
	�����e�Җ��̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_toukousya_style" size=120 value="$bbs1_toukousya_style"><br>
	���f�����̊�{�X�^�C���ݒ�<br>
	<input type=text name="bbs1_table2_style" size=120 value="$bbs1_table2_style"><br>
	�����e���̃T�C�Y�i���p�������Ŏw��j<br>
	<input type=text name="bbs1_toukouwidth" size=120 value="$bbs1_toukouwidth"><br>
	�������N�ia�^�O�j�̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_a_hover_style" size=120 value="$bbs1_a_hover_style"><br>
	���e�[�u���̉���<br>
	<input type=text name="bbs1_tablewidth" size=120 value="$bbs1_tablewidth"><br>
	��input��select�̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_siasenbako" size=120 value="$bbs1_siasenbako"><br>
	�����X�����̃X�^�C���ݒ�<br>
	<input type=text name="bbs1_yobi7" size=120 value="$bbs1_yobi7"><br>
	���f���������݂Ń����N�{�^�����g��<br><!-- koko2007/06/26 -->
	<input type=checkbox name="bbs_link" value="1"$bbs_link_check>�f���̃����N���g��<br>
EOM
	if ($in{'mode'} eq "admin_bbs"){
		print <<"EOM";
	�������X�̏Z����p�f���ɂ���i���̌f����ݒu�����X�ɏZ��ł���l�������{���E�������݂ł��܂��j<br>
	<select name="bbs1_yobi6">
	<option value="">�ʏ�</option>
EOM
	if ($bbs1_yobi6 eq "on"){
		print "<option value=\"on\" selected>�����X�̏Z����p</option>";
	}else{
		print "<option value=\"on\">�����X�̏Z����p</option>"
	}
	print "</select><br><br>";
	}
	
	print "<input type=submit value=�ݒ�ύX>";

		if ($in{'mode'} eq "admin_bbs"){
		print <<"EOM";
	<a href="$this_script?mode=normal_bbs&ori_ie_id=admin&bbs_num=$in{'bbs_num'}&name=$in{'name'}&admin_pass=$in{'admin_pass'}&con_sele=0" target=_blank>[���݂̐ݒ���e�̊m�F]</a>
	</td></tr></table>
	</form>
EOM
		}else{
		print <<"EOM";
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=0" target=_blank>[���݂̐ݒ���e�̊m�F]</a>
	</td></tr></table>
	</form>
EOM
		}
#koko2007/03/21
	if ($syokika){
		chomp $bbs_link; #koko2007/06/26
		$bbs_settei_temp = "$bbs1_title<>$bbs1_come<>$bbs1_body_style<>$bbs1_toukousya_style<>$bbs1_table2_style<>$bbs1_toukouwidth<>$bbs1_a_hover_style<>$bbs1_tablewidth<>$bbs1_title_style<>$bbs1_leed_style<>$bbs1_siasenbako<>$bbs1_yobi5<>$bbs1_yobi6<>$bbs1_yobi7<>$bbs1_yobi8<>$bbs1_yobi9<>$bbs1_yobi10<>$bbs_link<>\n"; #koko2007/06/26
		open(OLOUT,">$bbs1_settei_file") || &error("$bbs1_settei_file�ɏ������݂��o���܂���");
		eval{ flock (OLOUT, 2); };
		print OLOUT $bbs_settei_temp;
		close(OLOUT);
	}
#kokoend2007/03/21
}

sub bbs1_settei_do {
#�Ǘ��ҍ쐬BBS�̏ꍇ
	if ($in{'command'} eq "admin_bbs"){
		$bbs1_settei_file="./member/admin/bbs".$in{'bbs_num'}."_ini.cgi";
	}else{
		$bbs1_settei_file="./member/$in{'iesettei_id'}/bbs1_ini.cgi";
	}
		open(OIB,"< $bbs1_settei_file") || &error("Open Error : $bbs1_settei_file");
		eval{ flock (OIB, 1); };
			$bbs1_settei_data = <OIB>;
			($bbs1_title,$bbs1_come,$bbs1_body_style,$bbs1_toukousya_style,$bbs1_table2_style,$bbs1_toukouwidth,$bbs1_a_hover_style,$bbs1_tablewidth,$bbs1_title_style,$bbs1_leed_style,$bbs1_siasenbako,$bbs1_yobi5,$bbs1_yobi6,$bbs1_yobi7,$bbs1_yobi8,$bbs1_yobi9,$bbs1_yobi10,$bbs_link)= split(/<>/,$bbs1_settei_data); #koko2007/06/26
		close(OIB);
		chomp $bbs_link; #koko2007/06/26
		&lock;
			$bbs1_title = $in{'�^�C�g��'};
			$bbs1_come = $in{'�R�����g'};
			$bbs1_body_style = $in{'bbs1_body_style'};
			$bbs1_toukousya_style = $in{'bbs1_toukousya_style'};
			$bbs1_table2_style = $in{'bbs1_table2_style'};
			$bbs1_toukouwidth = $in{'bbs1_toukouwidth'};
			$bbs1_a_hover_style = $in{'bbs1_a_hover_style'};
			$bbs1_tablewidth = $in{'bbs1_tablewidth'};
			$bbs1_title_style = $in{'bbs1_title_style'};
			$bbs1_leed_style = $in{'bbs1_leed_style'};
			$bbs1_siasenbako = $in{'bbs1_siasenbako'};
			$bbs1_yobi5 = $in{'bbs1_yobi5'};
			$bbs1_yobi6 = $in{'bbs1_yobi6'};
			$bbs1_yobi7 = $in{'bbs1_yobi7'};
			$bbs1_yobi8 = $in{'bbs1_yobi8'};
			$bbs1_yobi9 = $in{'bbs1_yobi9'};
			$bbs1_yobi10 = $in{'bbs1_yobi10'};

			$bbs_link = $in{'bbs_link'}; #koko2007/06/26

		$bbs_settei_temp = "$bbs1_title<>$bbs1_come<>$bbs1_body_style<>$bbs1_toukousya_style<>$bbs1_table2_style<>$bbs1_toukouwidth<>$bbs1_a_hover_style<>$bbs1_tablewidth<>$bbs1_title_style<>$bbs1_leed_style<>$bbs1_siasenbako<>$bbs1_yobi5<>$bbs1_yobi6<>$bbs1_yobi7<>$bbs1_yobi8<>$bbs1_yobi9<>$bbs1_yobi10<>$bbs_link<>\n"; #koko2007/06/26
	open(OLOUT,">$bbs1_settei_file") || &error("$bbs1_settei_file�ɏ������݂��o���܂���");
	eval{ flock (OLOUT, 2); };
	print OLOUT $bbs_settei_temp;
	close(OLOUT);
		&unlock;
		if ($in{'command'} eq "admin_bbs"){
			&header;
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>�ݒ��ύX���܂����B</td></tr></table><br>
	
	<form method=POST action="$script">
	<input type=hidden name=mode value="admin_bbs">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>
EOM
	exit;
		}else{
			&my_house_settei;
		}
}

####�Ǝ�f���̐ݒ�
sub gentei_settei {
	$my_directry = "./member/$in{'iesettei_id'}";
	$gentei_settei_file="$my_directry/gentei_ini.cgi";
	if (! -e $gentei_settei_file){
		open(OIB,">$gentei_settei_file") || &error("Write Error : $gentei_settei_file");
		eval{ flock (OIB, 2); };
		chmod 0666,"$gentei_settei_file";
		close(OIB);
	}
	$gentei_log_file="$my_directry/gentei_log.cgi";
	if (! -e $gentei_log_file){
		open(OIL,">$gentei_log_file") || &error("Write Error : $gentei_log_file");
		eval{ flock (OIL, 2); };
		chmod 0666,"$gentei_log_file";
		close(OIL);
	}
		open(OIB,"< $gentei_settei_file") || &error("Open Error : $gentei_settei_file");
		eval{ flock (OIB, 1); };
			$gentei_settei_data = <OIB>;
			($gentei_title,$gentei_come,$gentei_body_style,$gentei_daimei_style,$gentei_table2_style,$gentei_kensuu,$gentei_tablewidth,$gentei_title_style,$gentei_leed_style,$gentei_siasenbako,$gentei_yobi5,$gentei_yobi6,$gentei_yobi7,$gentei_yobi8,$gentei_yobi9,$gentei_yobi10)= split(/<>/,$gentei_settei_data);
		close(OIB);
		
#�X�^�C���̏�����
	if ($gentei_body_style eq ""){$gentei_body_style = "background-color:#99cc99;";$syokika = 1;} #koko2007/03/21
	if ($gentei_title_style eq ""){$gentei_title_style = "font-size: 20px; color: #339966;line-height:150%; text-align:center;";}
	if ($gentei_leed_style eq ""){$gentei_leed_style = "font-size: 11px; color: #ff6600;line-height:160%;";}
	if ($gentei_daimei_style eq ""){$gentei_daimei_style = "font-size: 14px; color: #445555;line-height:200%;";}
	if ($gentei_table2_style eq ""){$gentei_table2_style = "font-size: 11px; line-height: 16px; color: #666666; background-color:#ffffcc; border: #339966; border-style: dotted; border-width:4px;";}
	if ($gentei_kensuu eq ""){$gentei_kensuu = "5";}
	if ($gentei_tablewidth eq ""){$gentei_tablewidth = "520";}
	if ($gentei_siasenbako eq ""){$gentei_siasenbako = "font-size:11px;color:#000000";}
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="gentei_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<div class=tyuu>���Ǝ�f���̐ݒ�</div>
	���f���̃^�C�g���i�^�O�w��B���URL�Ȃ�΃C���[�W�摜�̎w����j<br>
	<textarea  cols=80 rows=4 name="�^�C�g��" wrap="soft">$gentei_title</textarea><br>
	���^�C�g�����̃R�����g<br>
	<input type=text name="�R�����g" size=120  value=$gentei_come><br>
	���w�i�̃X�^�C���ݒ�<br>
	<input type=text name="gentei_body_style" size=120 value="$gentei_body_style"><br>
	���f���^�C�g���̃X�^�C���ݒ�<br>
	<input type=text name="gentei_title_style" size=120 value="$gentei_title_style"><br>
	���^�C�g�����̃R�����g�̃X�^�C���ݒ�<br>
	<input type=text name="gentei_leed_style" size=120 value="$gentei_leed_style"><br>
	���L���̑薼�̃X�^�C���ݒ�<br>
	<input type=text name="gentei_daimei_style" size=120 value="$gentei_daimei_style"><br>
	���f�����̊�{�X�^�C���ݒ�<br>
	<input type=text name="gentei_table2_style" size=120 value="$gentei_table2_style"><br>
	���P�y�[�W�ɕ\\������L�������i���p�������Ŏw��j<br>
	<input type=text name="gentei_kensuu" size=120 value="$gentei_kensuu"><br>
	���e�[�u���̉���<br>
	<input type=text name="gentei_tablewidth" size=120 value="$gentei_tablewidth"><br>
	��input��select�̃X�^�C���ݒ�<br>
	<input type=text name="gentei_siasenbako" size=120 value="$gentei_siasenbako"><br>
	<input type=submit value=�ݒ�ύX>
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=3" target=_blank>[���݂̐ݒ���e�̊m�F]</a>
	</form>
	
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="gentei_regist">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=ori_ie_id value="$k_id">
	<input type=hidden name=town_no value="$in{'town_no'}"><br><br>
	<div class=tyuu>�����e�i�^�O�j</div>
	�^�C�g��<br>
	<input type=text name="b_title" size=80><br>
	���e<br>
	<textarea  cols=90 rows=7 name="b_com" wrap="soft"></textarea><br>
	<input type=submit value="���e">
	</form>
	</td></tr></table>
	
EOM
#koko2007/03/21
	if ($syokika){
		$gentei_settei_temp = "$gentei_title<>$gentei_come<>$gentei_body_style<>$gentei_daimei_style<>$gentei_table2_style<>$gentei_kensuu<>$gentei_tablewidth<>$gentei_title_style<>$gentei_leed_style<>$gentei_siasenbako<>$gentei_yobi5<>$gentei_yobi6<>$gentei_yobi7<>$gentei_yobi8<>$gentei_yobi9<>$gentei_yobi10<>\n";
		open(OLOUT,">$gentei_settei_file") || &error("$gentei_settei_file�ɏ������݂��o���܂���");
		eval{ flock (OLOUT, 2); };
		print OLOUT $gentei_settei_temp;
		close(OLOUT);
	}
#kokoend
}

sub gentei_settei_do {
	$gentei_settei_file="./member/$in{'iesettei_id'}/gentei_ini.cgi";
		open(OIB,"< $gentei_settei_file") || &error("Open Error : $gentei_settei_file");
		eval{ flock (OIB, 1); };
			$gentei_settei_data = <OIB>;
			($gentei_title,$gentei_come,$gentei_body_style,$gentei_daimei_style,$gentei_table2_style,$gentei_kensuu,$gentei_tablewidth,$gentei_title_style,$gentei_leed_style,$gentei_siasenbako,$gentei_yobi5,$gentei_yobi6,$gentei_yobi7,$gentei_yobi8,$gentei_yobi9,$gentei_yobi10)= split(/<>/,$gentei_settei_data);
		close(OIB);
		
		&lock;
			$gentei_title = $in{'�^�C�g��'};
			$gentei_come = $in{'�R�����g'};
			$gentei_body_style = $in{'gentei_body_style'};
			$gentei_daimei_style = $in{'gentei_daimei_style'};
			$gentei_table2_style = $in{'gentei_table2_style'};
			$gentei_kensuu = $in{'gentei_kensuu'};
			$gentei_tablewidth = $in{'gentei_tablewidth'};
			$gentei_title_style = $in{'gentei_title_style'};
			$gentei_leed_style = $in{'gentei_leed_style'};
			$gentei_siasenbako = $in{'gentei_siasenbako'};
			$gentei_yobi5 = $in{'gentei_yobi5'};
			$gentei_yobi6 = $in{'gentei_yobi6'};
			$gentei_yobi7 = $in{'gentei_yobi7'};
			$gentei_yobi8 = $in{'gentei_yobi8'};
			$gentei_yobi9 = $in{'gentei_yobi9'};
			$gentei_yobi10 = $in{'gentei_yobi10'};
		$gentei_settei_temp = "$gentei_title<>$gentei_come<>$gentei_body_style<>$gentei_daimei_style<>$gentei_table2_style<>$gentei_kensuu<>$gentei_tablewidth<>$gentei_title_style<>$gentei_leed_style<>$gentei_siasenbako<>$gentei_yobi5<>$gentei_yobi6<>$gentei_yobi7<>$gentei_yobi8<>$gentei_yobi9<>$gentei_yobi10<>\n";
	open(OLOUT,">$gentei_settei_file") || &error("$gentei_settei_file�ɏ������݂��o���܂���");
	eval{ flock (OLOUT, 2); };
	print OLOUT $gentei_settei_temp;
	close(OLOUT);
		&unlock;
		&my_house_settei;
}


####���X�̐ݒ�
sub omise_settei {
	$my_directry = "./member/$in{'iesettei_id'}";
	$omise_settei_file="$my_directry/omise_ini.cgi";
	if (! -e $omise_settei_file){
		open(OIB,">$omise_settei_file") || &error("Write Error : $omise_settei_file");
		eval{ flock (OIB, 2); };
		chmod 0666,"$omise_settei_file";
		close(OIB);
	}
	$omise_log_file="$my_directry/omise_log.cgi";
	if (! -e $omise_log_file){
		open(OIL,">$omise_log_file") || &error("Write Error : $omise_log_file");
		eval{ flock (OIL, 2); };
		chmod 0666,"$omise_log_file";
		close(OIL);
	}
		open(OIB,"< $omise_settei_file") || &error("Open Error : $omise_settei_file");
		eval{ flock (OIB, 1); };
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
#omise_yobi5����{�̔��|�����@omise_yobi6�����i�J�e�S���[�̃X�^�C���ݒ�@omise_yobi7�������N�̃X�^�C��
		close(OIB);
		
#�X�^�C���̏�����
	if ($omise_yobi5 eq ""){$omise_yobi5 = "2";}
	if ($omise_body_style eq ""){$omise_body_style = "background-color:#ffcc33;";$syokika =1;} #koko2007/03/21
	if ($omise_title_style eq ""){$omise_title_style = "font-size: 18px; color: #ff6600; line-height:160%;";}
	if ($omise_leed_style eq ""){$omise_leed_style = "font-size: 11px; line-height: 16px; color: #000000";}
	if ($omise_table1_style eq ""){$omise_table1_style = "font-size: 11px; line-height: 18px; color: #666666; background-color:#ffffff; border: #666666; border-style: solid; border-width:1px";}
	if ($omise_table2_style eq ""){$omise_table2_style = "font-size: 10px; color: #336699; background-color:#ffffff; border: #666666; border-style: solid; border-width:1px";}
	if ($omise_syouhin_table eq ""){$omise_syouhin_table = "font-size: 11px; color: #333333; background-color:#ffffaa; ";}
	if ($omise_koumokumei eq ""){$omise_koumokumei = "font-size: 11px; color: #000000; background-color:#ffcc66; ";}
	if ($omise_yobi6 eq ""){$omise_yobi6 = "background-color:#ffff88;";}
	if ($omise_yobi7 eq ""){$omise_yobi7 = "font-size: 11px; color:#333333;text-decoration: none";}
	if ($omise_siasenbako eq ""){$omise_siasenbako = "font-size:11px;color:#000000";}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="omise_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<div class=tyuu>�����X�̐ݒ�</div>
	�����X�̃^�C�g���i�^�O�w��B���URL�Ȃ�΃C���[�W�摜�̎w����j<br>
	<textarea  cols=80 rows=4 name="�^�C�g��" wrap="soft">$omise_title</textarea><br>
	�����X�̎�ށi�X�[�p�[�͑S�Ă̏��i���������Ƃ��ł��܂����A�d����z���\\�����i��1.5�{�ɂȂ�܂��B�܂��A���Ƃł��X�̎�ނ�ς����ꍇ�A���ݎd����Ă��鏤�i�͑S�Ė����Ȃ�܂��̂ł����ӂ��������B�j<br>
	<select name="omise_syubetu">
EOM
	foreach (@global_syouhin_syubetu){
		print "<option value=$_";
		if ($omise_syubetu eq "$_"){print " selected"; $ori_ie_syubetu_0 = $omise_syubetu;} #koko2007/03/17
		print ">$_</option>\n";
	}
	print <<"EOM";
	</select>
	<br>
	�����X�̃R�����g<br>
	<textarea  cols=80 rows=3 name="�R�����g" wrap="soft">$omise_come</textarea><br>
	����{�̔��|�����i�f�p�[�g�ł͎d����l�̂R�{�̋��z�Ŕ����Ă��܂��B���̉��i��荂���ݒ肷�邱�Ƃ͂ł��܂���B���i���X�g�Ōʂɐݒ肷�邱�Ƃ��ł��܂��j<br>
	<input type=text name="omise_yobi5" size=120  value=$omise_yobi5><br>
	���w�i�̃X�^�C���ݒ�<br>
	<input type=text name="omise_body_style" size=120 value="$omise_body_style"><br>
	���^�C�g���̃X�^�C���ݒ�<br>
	<input type=text name="omise_title_style" size=120 value="$omise_title_style"><br>
	���R�����g�̃X�^�C���ݒ�<br>
	<input type=text name="omise_leed_style" size=120 value="$omise_leed_style"><br>
	���^�C�g�����e�[�u���̃X�^�C���ݒ�<br>
	<input type=text name="omise_table1_style" size=120 value="$omise_table1_style"><br>
	�����i���X�g�e�[�u���̘g����і}��̃X�^�C���ݒ�<br>
	<input type=text name="omise_table2_style" size=120 value="$omise_table2_style"><br>
	�����i���X�g�e�[�u�����X�^�C���ݒ�<br>
	<input type=text name="omise_syouhin_table" size=120 value="$omise_syouhin_table"><br>
	�����i���X�g�̍��ږ������̃X�^�C���ݒ�<br>
	<input type=text name="omise_koumokumei" size=120 value="$omise_koumokumei"><br>
	�����i�J�e�S���[�����̃X�^�C���ݒ�<br>
	<input type=text name="omise_yobi6" size=120 value="$omise_yobi6"><br>
	��input��select�̃X�^�C���ݒ�<br>
	<input type=text name="omise_siasenbako" size=120 value="$omise_siasenbako"><br>
	��a�^�O�̃X�^�C���ݒ�<br>
	<input type=text name="omise_yobi7" size=120 value="$omise_yobi7"><br>
	<input type=submit value=�ݒ�ύX>
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=1" target=_blank>[���݂̐ݒ���e�̊m�F]</a><br><br>
	</form>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="my_syouhin">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�d���ꂽ���i�̃��X�g">
	</form>
	<form method=POST action="$script">
	<input type=hidden name=mode value="orosi">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�d����ɏo������">�i�X�̉��≮�ɍs���j</form>
	<!-- koko2007/08/11 -->
	<form method="POST" action="tonyahenpin.cgi">
	<input type=hidden name=mode value="henpin">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�ԕi���s��"></form>
	</td></tr></table>
EOM
#koko2007/03/21
	if ($syokika){
		$omise_settei_temp = "$omise_title<>$omise_come<>$omise_body_style<>$omise_syubetu<>$omise_table1_style<>$omise_table2_style<>$omise_koumokumei<>$omise_syouhin_table<>$omise_title_style<>$omise_leed_style<>$omise_siasenbako<>$omise_yobi5<>$omise_yobi6<>$omise_yobi7<>$omise_yobi8<>$omise_yobi9<>$omise_yobi10<>\n";
		open(OLOUT,">$omise_settei_file") || &error("$omise_settei_file�ɏ������݂��o���܂���");
		eval{ flock (OLOUT, 2); };
		print OLOUT $omise_settei_temp;
		close(OLOUT);
	}#kokoend2007/03/21
#koko2007/03/17
	open(IN,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
	eval{ flock (IN, 1); };
	@ori_ie_para = <IN>;
	close(IN);
	@new_ori_ie_list3 = (); #koko2007/07/11
	foreach (@ori_ie_para){
		&ori_ie_sprit($_);
		if ($in{'iesettei_id'} eq $ori_k_id){		#ver.1.3
			$ori_ie_syubetu = $ori_ie_syubetu_0;
		}
		&ori_ie_temp;
		push (@new_ori_ie_list3,$ori_ie_temp);#koko2007/03/23
	}
#�ƃ��X�g�X�V
#koko2007/09/15
		$i=0;
		$nijyuu = 0;
		foreach (@new_ori_ie_list3){
			if ($_ eq $new_ori_ie_list3[0] && $i){
				$nijyuu = $i;
				&error("��d�������� o_h 3");
				last;
			}
			$i++;
		}
		if ($nijyuu){
			splice @new_ori_ie_list3,$nijyuu;
		}
#kokoend

	open(OIO,">$ori_ie_list") || &error("$ori_ie_list�ɏ������߂܂���");
	eval{ flock (OIO, 2); };
	print OIO @new_ori_ie_list3;#koko2007/03/23
	close(OIO);
#kokoend3/17
}

sub omise_settei_do {
	$omise_settei_file="./member/$in{'iesettei_id'}/omise_ini.cgi";
		open(OIB,"< $omise_settei_file") || &error("Open Error : $omise_settei_file");
		eval{ flock (OIB, 1); };
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
		close(OIB);
		
		&lock;
			$change_syubetu_flag = "";
			$omise_title = $in{'�^�C�g��'};
			$omise_come = $in{'�R�����g'};
			if ($omise_syubetu ne $in{'omise_syubetu'}){$change_syubetu_flag = "on";}
			$omise_syubetu = $in{'omise_syubetu'};
			$omise_body_style = $in{'omise_body_style'};
			$omise_table1_style = $in{'omise_table1_style'};
			$omise_table2_style = $in{'omise_table2_style'};
			$omise_koumokumei = $in{'omise_koumokumei'};
			$omise_syouhin_table = $in{'omise_syouhin_table'};
			$omise_title_style = $in{'omise_title_style'};
			$omise_leed_style = $in{'omise_leed_style'};
			$omise_siasenbako = $in{'omise_siasenbako'};
			if ($in{'omise_yobi5'} > 3){&error("�̔��|������3�{�ȉ��ɂ��Ă�������");}
			if ($in{'omise_yobi5'} <= 0){&error("�̔��|�������s�K�؂ł��B");}			#ver.1.3
			$omise_yobi5 = $in{'omise_yobi5'};
			$omise_yobi6 = $in{'omise_yobi6'};
			$omise_yobi7 = $in{'omise_yobi7'};
			$omise_yobi8 = $in{'omise_yobi8'};
			$omise_yobi9 = $in{'omise_yobi9'};
			$omise_yobi10 = $in{'omise_yobi10'};
		$omise_settei_temp = "$omise_title<>$omise_come<>$omise_body_style<>$omise_syubetu<>$omise_table1_style<>$omise_table2_style<>$omise_koumokumei<>$omise_syouhin_table<>$omise_title_style<>$omise_leed_style<>$omise_siasenbako<>$omise_yobi5<>$omise_yobi6<>$omise_yobi7<>$omise_yobi8<>$omise_yobi9<>$omise_yobi10<>\n";
	open(OLOUT,">$omise_settei_file") || &error("$omise_settei_file�ɏ������݂��o���܂���");
	eval{ flock (OLOUT, 2); };
	print OLOUT $omise_settei_temp;
	close(OLOUT);
#���X�̎�ޕύX�Ȃ珤�i���X�g��������
		if ($change_syubetu_flag eq "on"){
			$i = ""; 
			$omise_log_file="./member/$in{'iesettei_id'}/omise_log.cgi";
			open(SP,">$omise_log_file") || &error("Open Error : $omise_log_file");
			eval{ flock (SP, 2); };
			print SP $i;
			close(SP);
		}
		&unlock;
		&my_house_settei;
}


####�Ǝ�URL�̐ݒ�
sub dokuzi_settei {
	$my_directry = "./member/$in{'iesettei_id'}";
	$dokuzi_settei_file="$my_directry/dokuzi_ini.cgi";
	if (! -e $dokuzi_settei_file){
		open(OIB,">$dokuzi_settei_file") || &error("Write Error : $dokuzi_settei_file");
		eval{ flock (OIB, 2); };
		chmod 0666,"$dokuzi_settei_file";
		close(OIB);
	}
		open(OIB,"< $dokuzi_settei_file") || &error("Open Error : $dokuzi_settei_file");
		eval{ flock (OIB, 1); };
			$dokuzi_settei_data = <OIB>;
			($dokuzi_url,$dokuzi_width,$dokuzi_height,$dokuzi_haikei_style,$dokuzi_title,$dokuzi_come,$dokuzi_title_style,$dokuzi_leed_style,$dokuzi_siasenbako,$dokuzi_yobi10)= split(/<>/,$dokuzi_settei_data);
		close(OIB);
		
#�X�^�C���̏�����
	if ($dokuzi_haikei_style eq ""){$dokuzi_haikei_style = "background-color:#ffffff;";$syokika =1;} #koko2007/03/21
	if ($dokuzi_title_style eq ""){$dokuzi_title_style = "font-size: 16px; color: #666666;line-height:160%;";}
	if ($dokuzi_leed_style eq ""){$dokuzi_leed_style = "font-size: 11px; line-height: 16px; color: #336699";}
	if ($dokuzi_width eq ""){$dokuzi_width = "800";}
	if ($dokuzi_height eq ""){$dokuzi_height = "400";}
	if ($dokuzi_siasenbako eq ""){$dokuzi_siasenbako = "font-size:11px;color:#000000";}
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="dokuzi_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<div class=tyuu>���Ǝ�URL�̐ݒ�</div>
	���R�[�i�[�^�C�g���i�^�O�w��B���URL�Ȃ�΃C���[�W�摜�̎w����B�܂��w�肵�Ȃ��Ă�OK�ł��B�j<br>
	<textarea  cols=80 rows=4 name="�^�C�g��" wrap="soft">$dokuzi_title</textarea><br>
	��URL�w��<br>
	<input type=text name="dokuzi_url" size=120 value="$dokuzi_url"><br>
	���^�C�g�����̃R�����g<br>
	<input type=text name="�R�����g" size=120  value=$dokuzi_come><br>
	���w�i�̃X�^�C���ݒ�<br>
	<input type=text name="dokuzi_haikei_style" size=120 value="$dokuzi_haikei_style"><br>
	���^�C�g���̃X�^�C���ݒ�<br>
	<input type=text name="dokuzi_title_style" size=120 value="$dokuzi_title_style"><br>
	���^�C�g�����̃R�����g�̃X�^�C���ݒ�<br>
	<input type=text name="dokuzi_leed_style" size=120 value="$dokuzi_leed_style"><br>
	��IFRAME�̉��T�C�Y<br>
	<input type=text name="dokuzi_width" size=120 value="$dokuzi_width"><br>
	��IFRAME�̏c�T�C�Y<br>
	<input type=text name="dokuzi_height" size=120 value="$dokuzi_height"><br>
	�������K���̃X�^�C���ݒ�<br>
	<input type=text name="dokuzi_siasenbako" size=120 value="$dokuzi_siasenbako"><br>
	
	<input type=submit value=�ݒ�ύX>
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=2" target=_blank>[���݂̐ݒ���e�̊m�F]</a>
	</td></tr></table>
	</form>
EOM
#koko2007/03/21
	if ($syokika){
		$dokuzi_settei_temp = "$dokuzi_url<>$dokuzi_width<>$dokuzi_height<>$dokuzi_haikei_style<>$dokuzi_title<>$dokuzi_come<>$dokuzi_title_style<>$dokuzi_leed_style<>$dokuzi_siasenbako<>$dokuzi_yobi10<>\n";
		open(OLOUT,">$dokuzi_settei_file") || &error("$dokuzi_settei_file�ɏ������݂��o���܂���");
		eval{ flock (OLOUT, 2); };
		print OLOUT $dokuzi_settei_temp;
		close(OLOUT);
	}
#kokoend2007/03/21
}

sub dokuzi_settei_do {
	$dokuzi_settei_file="./member/$in{'iesettei_id'}/dokuzi_ini.cgi";
		open(OIB,"< $dokuzi_settei_file") || &error("Open Error : $dokuzi_settei_file");
		eval{ flock (OIB, 1); };
			$dokuzi_settei_data = <OIB>;
			($dokuzi_url,$dokuzi_width,$dokuzi_height,$dokuzi_haikei_style,$dokuzi_title,$dokuzi_come,$dokuzi_title_style,$dokuzi_leed_style,$dokuzi_siasenbako,$dokuzi_yobi10)= split(/<>/,$dokuzi_settei_data);
		close(OIB);
		
		&lock;
			$dokuzi_title = $in{'�^�C�g��'};
			$dokuzi_come = $in{'�R�����g'};
			$dokuzi_url = $in{'dokuzi_url'};
			$dokuzi_haikei_style = $in{'dokuzi_haikei_style'};
			$dokuzi_title_style = $in{'dokuzi_title_style'};
			$dokuzi_leed_style = $in{'dokuzi_leed_style'};
			$dokuzi_width = $in{'dokuzi_width'};
			$dokuzi_height = $in{'dokuzi_height'};
			$dokuzi_siasenbako = $in{'dokuzi_siasenbako'};
			$dokuzi_yobi10 = $in{'dokuzi_yobi10'};
		$dokuzi_settei_temp = "$dokuzi_url<>$dokuzi_width<>$dokuzi_height<>$dokuzi_haikei_style<>$dokuzi_title<>$dokuzi_come<>$dokuzi_title_style<>$dokuzi_leed_style<>$dokuzi_siasenbako<>$dokuzi_yobi10<>\n";
	open(OLOUT,">$dokuzi_settei_file") || &error("$dokuzi_settei_file�ɏ������݂��o���܂���");
	eval{ flock (OLOUT, 2); };
	print OLOUT $dokuzi_settei_temp;
	close(OLOUT);
		&unlock;
		&my_house_settei;
}

#######�Ƃ̕ύX
sub house_change{
#���p�̏ꍇ
	if ($in{'command'} eq "baikyaku"){
		&lock;
#�ƃ��X�g�ւ̏�������
		open(IN,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
		eval{ flock (IN, 1); };
		@ori_ie_para = <IN>;
		close(IN);
#koko2007/04/20
		@new_ori_ie_list = ();#koko2007/07/11
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($name eq "$ori_ie_name"){
#�^�E����񏑂������p�ɏ����擾
				$my_town_is = $ori_ie_town;
				$my_point_is = $ori_ie_sentaku_point;
#�^�E�����ɏ�������
				$write_town_data = "./log_dir/townlog". $my_town_is .".cgi";
				open(TWI,"< $write_town_data") || &error("Open Error : $write_town_data");
				eval{ flock (TWI, 1); };
				$hyouzi_town_hairetu = <TWI>;
				close(TWI);
				@town_sprit_matrix =  split(/<>/,$hyouzi_town_hairetu);
#koko2007/05/02-04
			#	if ($town_sprit_matrix[$my_point_is] !~ m/=/){
			#		$akichi = $town_sprit_matrix[$my_point_is];
			#	}else{
					($ori_ie_para_moto,$akichi) = split(/=/, $town_sprit_matrix[$my_point_is]);
					($ori_k_id_in,$syurui,$ori_k_no_in) = split(/_/, $ori_ie_para_moto);
			#	}

			#	($ori_ie_para_moto,$akichi) = split(/=/,$town_sprit_matrix[$my_point_is]); #koko2007/05/04
				if (!$akichi){$akichi = "��n";}
	#			if ($ori_ie_town eq "3"){ #koko2007/03/29 �X�̔ԍ�
	#				if (!$akichi){$akichi = "��n2";}
	#			}else{
	#				if (!$akichi){$akichi = "��n";}
	#			}
				$town_sprit_matrix[$my_point_is] = "$akichi";#koko2007/05/02
#kokoend
				$town_temp=join("<>",@town_sprit_matrix);
#�^�E�����X�V
				open(TWO,">$write_town_data") || &error("$write_town_data�ɏ������߂܂���");
				eval{ flock (TWO, 2); };
				print TWO $town_temp;
				close(TWO);

				if ($baikyku_syoumetu eq 'yes'){ #koko2007/06/17
					if (-e "./member/$ori_k_id_in/0_log.cgi") {unlink ("./member/$ori_k_id_in/0_log.cgi");}
					if (-e "./member/$ori_k_id_in/1_log.cgi") {unlink ("./member/$ori_k_id_in/1_log.cgi");}
					if (-e "./member/$ori_k_id_in/2_log.cgi") {unlink ("./member/$ori_k_id_in/2_log.cgi");}
					if (-e "./member/$ori_k_id_in/3_log.cgi") {unlink ("./member/$ori_k_id_in/3_log.cgi");} #koko2007/08/18
				}

				next;
			}
			&ori_ie_temp;
			push (@new_ori_ie_list,$ori_ie_temp);
		}
#kokoend2007/04/20

#�ƃ��X�g�X�V
#koko2007/09/15
		$i=0;
		$nijyuu = 0;
		foreach (@new_ori_ie_list){
			if ($_ eq $new_ori_ie_list[0] && $i){
				$nijyuu = $i;
				&error("��d�������� o_h 4");
				last;
			}
			$i++;
		}
		if ($nijyuu){
			splice @new_ori_ie_list,$nijyuu;
		}
#kokoend
		open(OIO,">$ori_ie_list") || &error("$ori_ie_list�ɏ������߂܂���");
		eval{ flock (OIO, 2); };
		print OIO @new_ori_ie_list;
		close(OIO);
#koko2006/12/13 �R���e���c�̏���
		open(IN,"< ./member/$in{'k_id'}/oriie_settei.cgi") || &error("Open Error : ./member/$in{'k_id'}/oriie_settei.cgi");
		eval{ flock (IN, 1); };
		$ie_dat = <IN>;
		close(IN);
		(@ie_hairet) = split(/<>/, $ie_dat);
		$ie_hairet[0] = "";
		$ie_hairet[1] = "";
		$ie_hairet[2] = "";
		$ie_hairet[3] = ""; #koko2007/08/18
		$ie_dat = join("<>",@ie_hairet);
		open(IN,"> ./member/$in{'k_id'}/oriie_settei.cgi") || &error("Open Error : ./member/$in{'k_id'}/oriie_settei.cgi");
		eval{ flock (IN, 2); };
		print IN $ie_dat;
		close(IN);
#kokoend
#�j���[�X�L�^
		if($machikakushi eq 'yes'){#koko2007/10/21
			if(!($town_hairetu[$my_town_is] eq $kakushimachi_name && $kakushimachi_name) || !($town_hairetu[$my_town_is] eq $kakushimachi_name1 && $kakushimachi_name1) || !($town_hairetu[$my_town_is] eq $kakushimachi_name2 && $kakushimachi_name2) || !($town_hairetu[$my_town_is] eq $kakushimachi_name3 && $kakushimachi_name3) || !($town_hairetu[$my_town_is] eq $kakushimachi_name4 && $kakushimachi_name4)){
			#	if (!($town_hairetu[$my_town_is] eq $kakushimachi_name)){ #koko2007/06/13
					&news_kiroku("��","$name���񂪁u$town_hairetu[$my_town_is]�v�̉Ƃ𔄋p���܂����B");	#ver.1.3
			#	}
			}
		}else{
			&news_kiroku("��","$name���񂪁u$town_hairetu[$my_town_is]�v�̉Ƃ𔄋p���܂����B");	#ver.1.3
		}
		&unlock;
#���O�X�V
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			$money += $town_tika_hairetu[$my_town_is] * 10000;
		}
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);
			
		&header("","sonomati");
		print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
�Ƃ𔄋p���܂����B
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>

	</body></html>
EOM
		exit;
	}
#�ύX����
	if ($in{'command'} eq "do_change"){
		if ($in{'matirank2'} eq ""){&error("�Ƃ̃����N���I������Ă��܂���");} #koko2007/08/02
		$kensetu_hiyou = ($ie_hash{$in{'iegazou'}} + $housu_nedan[$in{'matirank2'}])*10000;#koko2007/08/02
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			if ($kensetu_hiyou > $money){&error("����������܂���B");}
		}
		&lock;
#�ƃ��X�g�ւ̏�������
		open(IN,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
		eval{ flock (IN, 1); };
		@ori_ie_para = <IN>;
		close(IN);
		@new_ori_ie_list4 = (); #koko2007/07/11
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($in{'iesettei_id'} eq $ori_k_id){		#ver.1.3
				if ($in{'iegazou'} ne ""){
					$ori_ie_image = "$img_dir/$in{'iegazou'}";
				}
				if ($in{'matirank2'} ne "99"){#koko2007/08/02
					$ori_ie_rank2 = $in{'matirank2'};#koko2007/08/02
				}
			}
			&ori_ie_temp;
			push (@new_ori_ie_list4,$ori_ie_temp);#koko2007/03/23
		}
#�ƃ��X�g�X�V
#koko2007/09/15
		$i=0;
		$nijyuu = 0;
		foreach (@new_ori_ie_list4){
			if ($_ eq $new_ori_ie_list4[0] && $i){
				$nijyuu = $i;
				&error("��d�������� o_h 5");
				last;
			}
			$i++;
		}
		if ($nijyuu){
			splice @new_ori_ie_list4,$nijyuu;
		}
#kokoend

		open(OIO,">$ori_ie_list") || &error("$ori_ie_list�ɏ������߂܂���");
		eval{ flock (OIO, 2); };
		print OIO @new_ori_ie_list4;#koko2007/03/23
		close(OIO);

		&unlock;
#���O�X�V
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			$money -= $kensetu_hiyou;
		}
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);
			
		&header;
		print <<"EOM";
<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
�Ƃ̕ύX�����܂����B
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>

	</body></html>
EOM
		exit;
	}		#�ύX�����̏ꍇ�̕�
	
#�Ɖ摜���n�b�V������W�J
	&header(kentiku_style);
#koko2007/03/30
	@ie_keys = (); #koko2007/07/11
	@ie_values = (); #koko2007/07/11
	if ($in{'town_no'} eq $tokusyu_ie_no && $tokusyu_ie_no ne ''){
		while(($ie_key,$ie_val) = each %ie_hash2){
			push @ie_keys,$ie_key;
			push @ie_values,$ie_val;

		}
	}else{
		while(($ie_key,$ie_val) = each %ie_hash){
			push @ie_keys,$ie_key;
			push @ie_values,$ie_val;
		}
	}
#kokoend
	@ie_rank=@ie_keys[ sort {$ie_values[$a] <=> $ie_values[$b]} 0..$#ie_keys]; #koko2006/03/12

#		sub by_iekey{$ie_values[$a] <=> $ie_values[$b];}
#		@ie_rank=@ie_keys[ sort by_iekey 0..$#ie_keys]; 
	$i=1;
#koko2007/08/14
	if ($in{'town_no'} eq $tokusyu_ie_no && $tokusyu_ie_no ne ''){
		foreach(@ie_rank){
			$iegazou .= "<td align=center><input type=radio name=iegazou value=$_><br><img src=\"$img_dir/$_\" width=32 height=32><br>$ie_hash{$_}���~<br>$name_hash2{$_}\n";
			if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
			$i ++;
		}
	}else{
		foreach(@ie_rank){
			$iegazou .= "<td align=center><input type=radio name=iegazou value=$_><br><img src=\"$img_dir/$_\" width=32 height=32><br>$ie_hash{$_}���~<br>$name_hash{$_}\n";
			if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
			$i ++;
		}
	}
#kokoend
	$iegazou .= "<td align=center><input type=radio name=iegazou value=\"\"><br>����̂܂�\n";
	if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>�O�ρA�����̕ύX�́A���z���Ɠ��z�̔�p��������܂��B</td>
	</tr></table><br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change">
	<input type=hidden name=command value="do_change">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td valign=top>
	<div class=honbun2>���Ƃ̑I��</div>
	<table boader=0 cellspacing="0" cellpadding="5" width=100%><tr>
	$iegazou
	</tr></table><br>
	
	<table boader=0 cellspacing="0" cellpadding="5" width=100%><tr>
	<td><div class=honbun2>���Ƃ̃����N�i������j</div><br>
	<input type=radio name=matirank2 value="0">�`�����N�F$housu_nedan[0]���~�i�S�R���e���c�����\\�����\\�j<br>
	<input type=radio name=matirank2 value="1">�a�����N�F$housu_nedan[1]���~�i�R�R���e���c�����\\�����\\�j<br>
	<input type=radio name=matirank2 value="2">�b�����N�F$housu_nedan[2]���~�i�Q�R���e���c�����\\�����\\�j<br>
	<input type=radio name=matirank2 value="3">�c�����N�F$housu_nedan[3]���~�i�P�R���e���c�����\\�����\\�j<br>
	<input type=radio name=matirank2 value="99">����̂܂�
	</td></tr></table>
EOM
#��L�@name=matirank�@���@name=matirank2�@�ɕύX�@koko2007/08/02
	print <<"EOM";
	<br><br><div align=center><input type=submit value=" OK  "></div>
	</td></tr></table>
	<div align="center"><a href=\"javascript:history.back()\"> [�O�̉�ʂɖ߂�] </a></div>
	</body></html>
EOM
	exit;
}

#######�Ƃ̕ύX2 Koko2007/08/15
sub house_change2{
#���p�̏ꍇ
	if ($in{'iegazou'} eq "baikyaku"){
		&lock;
#�ƃ��X�g�ւ̏�������
		open(IN,"< $ori_ie_list") || &error("Open Error : $ori_ie_list");
		eval{ flock (IN, 1); };
		@ori_ie_para = <IN>;
		close(IN);

		@new_ori_ie_list = ();
		$ie_suu = "$in{'iesettei_id'}"."_"."$in{'iesuu'}";
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($ori_k_id eq $ie_suu){ #koko2007/08/15
#�^�E����񏑂������p�ɏ����擾
				$my_town_is = $ori_ie_town;
				$my_point_is = $ori_ie_sentaku_point;
#�^�E�����ɏ�������
				$write_town_data = "./log_dir/townlog". "$my_town_is" .".cgi"; #koko2007/08/18
				open(TWI,"< $write_town_data") || &error("Open Error : $write_town_data");
				eval{ flock (TWI, 1); };
				$hyouzi_town_hairetu = <TWI>;
				close(TWI);
				@town_sprit_matrix =  split(/<>/,$hyouzi_town_hairetu);
				($ori_ie_para_moto,$akichi) = split(/=/, $town_sprit_matrix[$my_point_is]);
				($ori_k_id_in,$syurui,$ori_k_no_in) = split(/_/, $ori_ie_para_moto);
				if (!$akichi){$akichi = "��n";}
				$town_sprit_matrix[$my_point_is] = "$akichi";#koko2007/05/02
				$town_temp=join("<>",@town_sprit_matrix);
#�^�E�����X�V
				open(TWO,">$write_town_data") || &error("$write_town_data�ɏ������߂܂���");
				eval{ flock (TWO, 2); };
				print TWO $town_temp;
				close(TWO);

				next;
			}
			&ori_ie_temp;
			push (@new_ori_ie_list,$ori_ie_temp);
		}

#�ƃ��X�g�X�V
#koko2007/09/15
		$i=0;
		$nijyuu = 0;
		foreach (@new_ori_ie_list){
			if ($_ eq $new_ori_ie_list[0] && $i){
				$nijyuu = $i;
				&error("��d�������� o_h 6");
				last;
			}
			$i++;
		}
		if ($nijyuu){
			splice @new_ori_ie_list,$nijyuu;
		}
#kokoend


		open(OIO,">$ori_ie_list") || &error("$ori_ie_list�ɏ������߂܂���");
		eval{ flock (OIO, 2); };
		print OIO @new_ori_ie_list;
		close(OIO);
#�j���[�X�L�^
		if($machikakushi eq 'yes'){ #koko2007/10/21
			if(!($town_hairetu[$my_town_is] eq $kakushimachi_name && $kakushimachi_name) || !($town_hairetu[$my_town_is] eq $kakushimachi_name1 && $kakushimachi_name1) || !($town_hairetu[$my_town_is] eq $kakushimachi_name2 && $kakushimachi_name2) || !($town_hairetu[$my_town_is] eq $kakushimachi_name3 && $kakushimachi_name3) || !($town_hairetu[$my_town_is] eq $kakushimachi_name4 && $kakushimachi_name4)){

		#	if (!($town_hairetu[$my_town_is] eq $kakushimachi_name && $machikakushi eq 'yes')){ #koko2007/06/13
				&news_kiroku("��","$name���񂪁u$town_hairetu[$my_town_is]�v�̉Ƃ𔄋p���܂����B");		#ver.1.3
			}
#koko2007/10/29
		}else{ #koko2007/10/30
			&news_kiroku("��","$name���񂪁u$town_hairetu[$my_town_is]�v�̉Ƃ𔄋p���܂����B");		#ver.1.3
		}
		&unlock;
#���O�X�V
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			$money += $town_tika_hairetu[$my_town_is] * 10000;
		}
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);
			
		&header("","sonomati");
		print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
�Ƃ𔄋p���܂����B
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>

	</body></html>
EOM
		exit;
	}

#�ύX����
	if ($in{'command'} eq "do_change2"){
		$kensetu_hiyou = $ie_hash{$in{'iegazou'}};
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			if ($kensetu_hiyou > $money){&error("����������܂���B");}
		}
		&lock;
#�ƃ��X�g�ւ̏�������
		$ori_ie_fail = "./log_dir/ori_ie_log.cgi"; #koko2007/08/15
		open(IN,"< $ori_ie_fail") || &error("Open Error : $ori_ie_list"); #koko2007/08/15
		eval{ flock (IN, 1); };
		@ori_ie_para = <IN>;
		close(IN);
		@new_ori_ie_list5 = ();


		$ie_suu = "$in{'iesettei_id'}"."_"."$in{'iesuu'}";

		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($ori_k_id eq $ie_suu){
				if ($in{'iegazou'} ne ""){
					$ori_ie_image = "$img_dir/$in{'iegazou'}";
				}
			}
			&ori_ie_temp;
			push (@new_ori_ie_list5,$ori_ie_temp);
		}
#�ƃ��X�g�X�V
		open(OIO,">$ori_ie_fail") || &error("$ori_ie_fail�ɏ������߂܂���"); #koko2007/08/15
		eval{ flock (OIO, 2); };
		print OIO @new_ori_ie_list5;
		close(OIO);

		&unlock;
#���O�X�V
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			$money -= $kensetu_hiyou;
		}
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);
			
		&header;
		print <<"EOM";
<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
�Ƃ̕ύX�����܂����B
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>

	</body></html>
EOM
		exit;
	}		#�ύX�����̏ꍇ�̕�
#�Ɖ摜���n�b�V������W�J
	&header(kentiku_style);
	@ie_keys = ();
	@ie_values = ();
	if ($in{'town_no'} eq $tokusyu_ie_no && $tokusyu_ie_no ne ''){
		while(($ie_key,$ie_val) = each %ie_hash2){
			push @ie_keys,$ie_key;
			push @ie_values,$ie_val;

		}
	}else{
		while(($ie_key,$ie_val) = each %ie_hash){
			push @ie_keys,$ie_key;
			push @ie_values,$ie_val;
		}
	}
	@ie_rank=@ie_keys[ sort {$ie_values[$a] <=> $ie_values[$b]} 0..$#ie_keys]; #koko2006/03/12

	$i=1;
	if ($in{'town_no'} eq $tokusyu_ie_no && $tokusyu_ie_no ne ''){
		foreach(@ie_rank){
			$ie_hash{$_} =int($ie_hash{$_} * $ie_bairitu);
			$iegazou .= "<td align=center><input type=radio name=iegazou value=$_><br><img src=\"$img_dir/$_\" width=32 height=32><br>$ie_hash{$_}���~<br>$name_hash2{$_}\n";
			if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
			$i ++;
		}
	}else{
		foreach(@ie_rank){
			$ie_hash{$_} =int($ie_hash{$_} * $ie_bairitu);
			$iegazou .= "<td align=center><input type=radio name=iegazou value=$_><br><img src=\"$img_dir/$_\" width=32 height=32><br>$ie_hash{$_}���~<br>$name_hash{$_}\n";
			if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
			$i ++;
		}
	}
	$disp_sentaku = $in{'iesuu'} +1;
	$iegazou .= "<td align=center><input type=radio name=iegazou value=\"\"><br>����̂܂�\n";
	if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>�O�ρA�����̕ύX�́A���z���Ɠ��z�̔�p��������܂��B</td>
	</tr></table><br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change2">
	<input type=hidden name=command value="do_change2">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
<input type=hidden name=iesuu value="$in{'iesuu'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td valign=top>
	<div class=honbun2>���Ƃ̑I�� $disp_sentaku</div>
	<table boader=0 cellspacing="0" cellpadding="5" width=100%><tr>
	$iegazou
	<td align=center><input type=radio name=iegazou value="baikyaku"><br>���p
	</tr></table><br>
	
	<br><br><div align=center><input type=submit value=" OK  "></div>
	</td></tr></table>
	<div align="center"><a href=\"javascript:history.back()\"> [�O�̉�ʂɖ߂�] </a></div>
	</body></html>
EOM
	exit;
}

#####�K�⏈��
sub houmon {
#koko2007/04/20
	($in{'ori_ie_id'},$bangou) = split(/_/, $in{'ori_ie_id'});
	if ($bangou == 1){&unei_2;} #koko2007/04/21 koko2007/04/30 koko2007/09/08
#kokoend
	if ($bangou == 2){&kaishiya;} #koko2007/05/05
	if ($bangou == 3){&motimono_hanbai;} #koko2007/09/08

	$houmonsaki_settei_file = "./member/$in{'ori_ie_id'}/oriie_settei.cgi";
	open(HS,"< $houmonsaki_settei_file") || &error("�܂��H�����ł�");
	eval{ flock (HS, 1); };
	$kihon_oriie_settei = <HS>;
	&oriie_settei_sprit ($kihon_oriie_settei);
	close(HS);
	if ($my_con1 eq ""){&error("�܂��l�Ɍ�������Ƃł͖����悤�ł��B");}		#ver.1.30
	
#�����K����ϐ��ɓ����
$saisenbako_data =<<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="saisensuru">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<select name=saisengaku>
	<option value=100>100�~</option>
	<option value=500>500�~</option>
	<option value=1000>1000�~</option>
	<option value=2000>2000�~</option>
	<option value=5000>5000�~</option>
	<option value=10000>10000�~</option>
	</select>
	<input type=submit value="�����K����">
	</form>
EOM

	if ($my_con1_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=\"houmon\"><input type=hidden name=ori_ie_id value=\"$in{'ori_ie_id'}\"><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=k_id value=\"$in{'k_id'}\"><input type=hidden name=con_sele value=\"$my_con1\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=submit value=\"$my_con1_title\"></form></td>\n";
	}
	
	if ($my_con2_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=\"houmon\"><input type=hidden name=ori_ie_id value=\"$in{'ori_ie_id'}\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=k_id value=\"$in{'k_id'}\"><input type=hidden name=con_sele value=\"$my_con2\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=submit value=\"$my_con2_title\"></form></td>\n";
	}
	
	if ($my_con3_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=\"houmon\"><input type=hidden name=ori_ie_id value=\"$in{'ori_ie_id'}\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=k_id value=\"$in{'k_id'}\"><input type=hidden name=con_sele value=\"$my_con3\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=submit value=\"$my_con3_title\"></form></td>\n";
	}
	
	if ($my_con4_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=\"houmon\"><input type=hidden name=ori_ie_id value=\"$in{'ori_ie_id'}\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=con_sele value=\"$my_con4\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=submit value=\"$my_con4_title\"></form></td>\n";
	}
	
	if ($in{'con_sele'} eq ""){
		if ($my_con1 eq "0"){&normal_bbs;}
		elsif  ($my_con1 eq "1"){&omise;}
		elsif  ($my_con1 eq "2"){&dokuzi_url;}
		elsif  ($my_con1 eq "3"){&gentei;}
	}elsif  ($in{'con_sele'} eq "0"){&normal_bbs;}
	elsif  ($in{'con_sele'} eq "1"){&omise;}
	elsif  ($in{'con_sele'} eq "2"){&dokuzi_url;}
	elsif  ($in{'con_sele'} eq "3"){&gentei;}
}

#####�ʏ��BBS
sub normal_bbs {
	if ($tajuukinsi_flag==1){
		if($k_yobi3 ne ""){
			&error("���d�o�^�͋֎~����Ă��܂��B<br>$k_yobi3");
		}
	}
	if ($tajuukinsi_flag==1){&tajuucheck;}
#ver.1.30��������
	$genzai_zikoku = time;
	open(GUEST,"< $guestfile");
	eval{ flock (GUEST, 1); };
	@all_guest=<GUEST>;
	close(GUEST);
	@new_all_guest = ();
	foreach (@all_guest) {
		($sanka_timer,$sanka_name,$hyouzi_check) = split(/<>/);
		if ($name eq "$sanka_name"){
			$sanka_timer = $genzai_zikoku;
		}
		$sanka_tmp = "$sanka_timer<>$sanka_name<>$hyouzi_check<>\n";
		push (@new_all_guest,$sanka_tmp);
	}
#ver.1.40��������
	if ($mem_lock_num == 0){
		$err = &data_save($guestfile, @new_all_guest);
		if ($err) {&error("$err");}
	}else{
		&lock;	
		open(GUEST,">$guestfile");
		eval{ flock (GUEST, 2); };
		print GUEST @new_all_guest;
		close(GUEST);
		&unlock;
	}
#ver.1.40�����܂�
#ver.1.30�����܂�
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_settei_file = "./member/admin/bbs".$in{'bbs_num'}."_ini.cgi";
	}else{
		$bbs1_settei_file = "./member/$in{'ori_ie_id'}/bbs1_ini.cgi";
	}
		open(OIB,"< $bbs1_settei_file") || &error("Open Error : $bbs1_settei_file");
		eval{ flock (OIB, 1); };
			$bbs1_settei_data = <OIB>;
			($bbs1_title,$bbs1_come,$bbs1_body_style,$bbs1_toukousya_style,$bbs1_table2_style,$bbs1_toukouwidth,$bbs1_a_hover_style,$bbs1_tablewidth,$bbs1_title_style,$bbs1_leed_style,$bbs1_siasenbako,$bbs1_yobi5,$bbs1_yobi6,$bbs1_yobi7,$bbs1_yobi8,$bbs1_yobi9,$bbs1_yobi10,$bbs_link)= split(/<>/,$bbs1_settei_data); #koko2007/06/26
		close(OIB);
		chomp $bbs_link; #koko2007/06/26
#�Z����p�f���̏ꍇ�`�F�b�N
	if ($bbs1_yobi6 eq "on"){
		if ($in{'admin_pass'} ne $admin_pass){
			&my_town_check($name);
			if ($return_my_town eq "no_town"){&error("���̊X�ɏZ��ł���l�ȊO�͌��邱�Ƃ��ł��܂���");}
			if ($return_my_town ne "$in{'town_no'}"){&error("���̊X�ɏZ��ł���l�ȊO�͌��邱�Ƃ��ł��܂���");}
		}
	}
	&ori_header("$bbs1_body_style","$bbs1_siasenbako","$bbs1_a_hover_style");

	print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM
	
	print <<"EOM";
	<br><table width="$bbs1_tablewidth" border="0" cellspacing="0" cellpadding="14" align=center style="$bbs1_table2_style">
	<tr><td>
	<div style = "$bbs1_title_style">$bbs1_title</div>
	<div style = "$bbs1_leed_style">$bbs1_come</div>
	</td></tr>
	<td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="bbs_regist">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=job value="$job">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<textarea cols="$bbs1_toukouwidth" rows="4" name="b_com" wrap="soft"></textarea>
	<input type=submit value="�V�K���e">
	</form>
EOM
	$page=$in{'page'};	
	if ($page eq "") { $page = 0; }
	$i=0;
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_log_file = "./member/admin/bbs".$in{'bbs_num'}."_log.cgi";
	}else{
		$bbs1_log_file = "./member/$in{'ori_ie_id'}/bbs1_log.cgi";
	}
	open(IN,"< $bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	eval{ flock (IN, 1); };
	@bbs_alldata=<IN>;
	close(IN);
	
#koko2006/11/23
	if ($in{'ori_ie_id'} eq $k_id){
		($total_counter,$all_total_counter,$kakikomijikan,$yomidashijikan,$bbs_id)= split(/<>/, $bbs_alldata[0]);
		chomp $bbs_id;
		if ($kakikomijikan > $yomidashijikan){
			$ima_time = time;
			$bbs_alldata[0] = "$total_counter<>$all_total_counter<>$kakikomijikan<>$ima_time<>$bbs_id<>\n";
			open(IN,"> $bbs1_log_file") || &error("Open Error : $bbs1_log_file");
			eval{ flock (IN, 2); };
			print IN @bbs_alldata;
			close(IN);
		}
	}
#kokoend
#koko2006/12/11
	foreach (@bbs_alldata){
		($b_num,$b_name,$b_date,$b_res,$b_mail,$b_com,$b_id)= split(/<>/);#koko2006/12/11
		if ($b_num){$i++;}
		if ($i == 1){next;}
		if ($i < $page + 1) { next; }
		if ($i > $page + 10) { last; }
#koko2006/12/16
		$b_id =~ s/[^0-9]//g;
		if ($b_id ne ""){
			if (not(-e "./member/$b_id/oriie_settei.cgi")){$b_id = "";}
			if ($b_id ne ""){
				open(IN,"< ./member/$b_id/oriie_settei.cgi") || &error("Open Error : ./member/$b_id/oriie_settei.cgi");
				eval{ flock (IN, 1); };
				$ie_dat = <IN>;
				close(IN);
				(@ie_hairet) = split(/<>/, $ie_dat);
				if (!($ie_hairet[0] eq "0" || $ie_hairet[1] eq "0" || $ie_hairet[2] eq "0" || $ie_hairet[3] eq "0")){ $b_id = "";}
			}
		}
#kokoend
		if ($b_res){

#	($bbc_name,@sonota) = split(/</, $b_name);
#	$bbs_name2 = join ("<",@sonota);
#	$bbs_name2 = "<".$bbs_name2;
			print "<div><span style=\"$bbs1_toukousya_style\">\n";
			if ($b_id ne "" && ($linkbotan eq 'yes' || $bbs_link)){
				print <<"EOM";
<form method=POST action="original_house.cgi" style="margin-top:0; margin-bottom:0;">
<input type=hidden name=mode value="houmon">
<input type=hidden name=ori_ie_id value="$b_id">
<input type=hidden name=name value="$name">
<input type=hidden name=pass value="$pass">
<input type=hidden name=k_id value="$in{'k_id'}">
<input type=hidden name=con_sele value="0">
<input type=hidden name=town_no value="$in{'town_no'}">
<input type=image src="./img/go.gif" alt="�f���ɔ�т܂��B">
$b_name</form>
EOM
			}else{
				print "$b_name";
			}
				print <<"EOM";
</span>�F$b_com</xmp>�i$b_date�j<span style=\"font-size:9px\">�L��no.$b_mail</span></div>
EOM
#kokoend
		}else{
	
#	($bbc_name,@sonota) = split(/</, $b_name);
#	$bbs_name2 = join ("<",@sonota);
#	$bbs_name2 = "<".$bbs_name2;

			print <<"EOM";
	<br><hr size=1><br>
	<div><span style="$bbs1_yobi5">NO.$b_num</span><br> <span style="$bbs1_toukousya_style">
EOM
			if ($b_id ne "" && ($linkbotan eq 'yes' || $bbs_link)){
				print <<"EOM";
<form method=POST action="original_house.cgi" style="margin-top:0; margin-bottom:0;">
<input type=hidden name=mode value="houmon">
<input type=hidden name=ori_ie_id value="$b_id">
<input type=hidden name=name value="$name">
<input type=hidden name=pass value="$pass">
<input type=hidden name=k_id value="$in{'k_id'}">
<input type=hidden name=con_sele value="0">
<input type=hidden name=town_no value="$in{'town_no'}">
<input type=image src="./img/go.gif" alt="�f���ɔ�т܂��B">
$b_name</form>
EOM
			}else{
				print "$b_name";
			}
			print <<"EOM";
</span>�F$b_com</span></xmp>�i$b_date�j<span style=\"font-size:9px\">�L��no.$b_mail</span>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="bbs_regist">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=job value="$job">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=b_res value="$b_num">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<textarea rows=2 name=b_com cols=50 ></textarea> <input type=submit value="���X">
	</form></div>
EOM
#koko2006/12/12 ��@text <textarea �ɕύX
		}
	}		#foreach��
	
		$next = $page + 10;
		$back = $page - 10;
		print "<div align=center><table border=0><tr>";
		if ($back >= 0) {
#�Ǘ���BBS�̏ꍇ
				if($in{'ori_ie_id'} eq "admin"){
					print <<"EOM";
			<form method=POST action="$this_script">
			<input type=hidden name=mode value="normal_bbs">
			<input type=hidden name=ori_ie_id value="admin">
			<input type=hidden name=bbs_num value="$in{'bbs_num'}">
<input type=hidden name=k_id value="$in{'k_id'}">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
			<input type=hidden name=town_no value="$in{'town_no'}">
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK">
			</form>
EOM
				}else{
#�l�̉Ƃ�BBS�̏ꍇ
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="houmon">
			<input type=hidden name=con_sele value="0">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
			<input type=hidden name=town_no value="$in{'town_no'}">
			<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK"></form></td>
EOM
				}
		}
		if ($next < $i) {
				if($in{'ori_ie_id'} eq "admin"){
					print <<"EOM";
			<form method=POST action="$this_script">
			<input type=hidden name=mode value="normal_bbs">
			<input type=hidden name=ori_ie_id value="admin">
			<input type=hidden name=bbs_num value="$in{'bbs_num'}">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
			<input type=hidden name=town_no value="$in{'town_no'}">
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT">
</form>
EOM
				}else{
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="houmon">
			<input type=hidden name=con_sele value="0">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
			<input type=hidden name=town_no value="$in{'town_no'}">
			<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT"></form></td>
EOM
				}
		}
		print "</tr></table></div>";
	print <<"EOM"; #koko2007/09/17
	</td></tr></table>
	<table width="$bbs1_tablewidth" border="0" cellspacing="0" cellpadding="0" align=center>
	<tr><td>
	<form method="POST" action="$this_script">
	<div style=" font-size: 10px; color: #444444"><br>
	<center>
	<input type=hidden name=mode value="bbs_delete">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	</xmp>�L��no. <input type=text name=b_count size=8>
	<input type=submit value="�폜">

	�e�L��no. <input type=text name=oya_count size=8>
	<input type=submit value="�폜">
	<input type=submit name= all_del value=" �S�L���폜" >

	</center>
	<br>���Q�[���Ǘ��҂̂݁u�L��no.�v���w�肵�ċL�����폜���邱�Ƃ��ł��܂��B<br>
	�����e���邱�Ƃł����𓾂邱�Ƃ��ł��܂����A���Ӗ��Ȕ����A�r�炵�s�ׂȂǕs�K�؂ȓ��e���������ꍇ�A�����A�z�X�g�̌��J�A�A�N�Z�X���ۂȂǂ̃y�i���e�B������܂��̂ł����ӂ��������B</div>
	</form></td></tr><tr><td>
	<br><div style=" font-size: 11px;" align="center"><a href="javascript:history.back()"> [�O�̉�ʂɖ߂�] </a></div>
	</td></tr>
	</table>
EOM
	if ($in{'ori_ie_id'} eq "admin"){
		&hooter("login_view","�߂�");
	}else{
		&hooter("login_view","�Ƃ��o��");
	}
exit;
}


#BBS���e����
sub bbs_regist {
	&lock;
#���O�t�@�C���X�V
	# ���O��ǂݍ���
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_log_file = "./member/admin/bbs".$in{'bbs_num'}."_log.cgi";
	}else{
		$bbs1_log_file = "./member/$in{'ori_ie_id'}/bbs1_log.cgi";
	}
	open(IN,"< $bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	eval{ flock (IN, 1); };
	# �擪�s���擾
	$total_counter = <IN>;
	($total_counter,$all_total_counter,$kakikomijikan,$yomidashijikan,$bbs_id) = split(/<>/, $total_counter);		#ver.1.40
	chomp $bbs_id;
	$top = <IN>;
	local($b_num,$b_name,$b_date,$b_res,$b_count,$b_com,$b_id)= split(/<>/, $top);#koko2006/12/11		#ver.1.40
	close(IN);

	if (length($in{'b_com'}) > 2000) {&error("���A�͑S�p1000�����p2000���ȓ��ł�");} #koko2006/12/12

	
	$in{'b_com'} =~ s/<>/&lt;&gt;/g;

#�^�O�֎~����
#		$in{'b_com'} =~ s/</&lt;/g;
#		$in{'b_com'} =~ s/>/&gt;/g;
# �R�����g�̉��s����
	$in{'b_com'} =~ s/\r\n/<br>/g;
	$in{'b_com'} =~ s/\r/<br>/g;
	$in{'b_com'} =~ s/\n/<br>/g;
	$in{'b_com'} =~ s/<plaintext/System�Fplaintext�^�O�̎g�p�͂�߂܂��傤�B/gi;
	$in{'b_com'} =~ s/<script/System�FJavaScript�͊�Ȃ�����֎~�B���߂�ˁB/gi;
		$in{'b_com'} =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
#ver.1.30��������
	$name_seikei = $in{'name'} . "<span style=\"font-size:9px\">�i$in{'job'}�j</span>";
	if ($name_seikei eq "$b_name" && $in{'b_com'} eq "$b_com") {
		&error("��d���e�ł�");
	}
#ver.1.30�����܂�
	if ($in{'b_com'} eq "") {
		&error("�R�����g�����͂���Ă��܂���");
	}

	open(IN,"< $bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	eval{ flock (IN, 1); };
	@all_data = <IN>;
	shift @all_data;
	$total_kizisuu = @all_data;
	close(IN);
	
	&time_get;
	$all_total_counter ++;		#�g�[�^���L�������J�E���gver.1.40
#�V�K���e�Ȃ�V�L��No���擾
	if ($in{'b_res'} eq ""){
		$total_counter++;
#�X�V�z����`
		$new_toukou = "$total_counter<>$in{'name'}<span style=\"font-size:9px\">�i$in{'job'}�j</span><>$date2<>$in{'b_res'}<>$all_total_counter<>$in{'b_com'}<>$in{'k_id'}<>\n"; #koko2006/12/11		#ver.1.40

		unshift (@all_data,$new_toukou);
#koko2006/11/23
		$ima_time = time;
		$total_counter = "$total_counter<>$all_total_counter<>$ima_time<>$yomidashijikan<>$in{'k_id'}<>\n"; #koko2006/12/11		#ver.1.40
#kokoend
		unshift (@all_data,$total_counter);
	
#���X�̏ꍇ
	}else{
#�X�V�z����`
			$new_toukou = "<>$in{'name'}<span style=\"font-size:9px\">�i$in{'job'}�j</span><>$date2<>$in{'b_res'}<>$all_total_counter<>$in{'b_com'}<>$in{'k_id'}<>\n";		#ver.1.40 #koko2006/12/11
		foreach (@all_data){
			($b_num,$b_name,$b_date,$b_res,$b_mail,$b_com,$b_id)= split(/<>/, $_);#koko2006/12/11
			if ($b_num eq "$in{'b_res'}" || $b_res eq "$in{'b_res'}"){push (@top_idou ,$_);	next;}
			push (@new_all_data,$_);
		}
		push (@top_idou ,$new_toukou);	
#koko2006/11/23
		$ima_time = time;
		unshift (@new_all_data,@top_idou);
		$total_counter = "$total_counter<>$all_total_counter<>$ima_time<>$yomidashijikan<>$in{'k_id'}<>\n"; #koko2006/12/11		#ver.1.40
#kokoend
		unshift (@new_all_data,$total_counter);
		@all_data = ();
		@all_data = @new_all_data;
	}		#���X�̏ꍇ��
	
	if ($total_kizisuu >= $bbs_kizi_max){pop @all_data;}
# ���O���X�V
	open(OUT,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
	eval{ flock (OUT, 2); };
	print OUT @all_data;
	close(OUT);
	
#�X�̔ɉh�x�A�b�v
	&town_haneiup($in{'town_no'});

# ���b�N����
	&unlock;
	
#�������Q�b�g
	$randed += int(rand(10))+1;
	if ($randed == 7){
		$randed += int(rand(10000))+5000;
		$money += $randed;
		$message_in = "���{�[�i�X�ł��I$randed�~�̂������Q�b�g���܂����B";
	}else{
		$randed += int(rand(2000))+1000;
		$money += $randed;
		$message_in = "��$randed�~�̂����𓾂܂����B";
	}
	&temp_routin;
	&log_kousin($my_log_file,$k_temp);
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
$message_in
</span>
</td></tr></table>
<br>
	<form method=POST action="$this_script">
EOM
	if ($in{'ori_ie_id'} eq "admin"){
		print "<input type=hidden name=mode value=\"normal_bbs\">";
	}else{
		print "<input type=hidden name=mode value=\"houmon\">";
	}

	print <<"EOM";
	<input type=hidden name=con_sele value="0">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>
EOM
	exit;
}

#####�Ǝ�f����
sub gentei {
	$gentei_settei_file = "./member/$in{'ori_ie_id'}/gentei_ini.cgi";
		open(OIB,"< $gentei_settei_file") || &error("Open Error : $gentei_settei_file");
		eval{ flock (OIB, 1); };
			$gentei_settei_data = <OIB>;
			($gentei_title,$gentei_come,$gentei_body_style,$gentei_daimei_style,$gentei_table2_style,$gentei_kensuu,$gentei_tablewidth,$gentei_title_style,$gentei_leed_style,$gentei_siasenbako,$gentei_yobi5,$gentei_yobi6,$gentei_yobi7,$gentei_yobi8,$gentei_yobi9,$gentei_yobi10)= split(/<>/,$gentei_settei_data);
		close(OIB);
	&ori_header("$gentei_body_style","$gentei_siasenbako");

	print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM

	print <<"EOM";
	<table width="$gentei_tablewidth" border="0" cellspacing="0" cellpadding="8" align=center style="$gentei_table2_style">
	<tr><td>
	<div style = "$gentei_title_style">$gentei_title</div>
	<div style = "$gentei_leed_style">$gentei_come</div>
	</td></tr>
	<td>
EOM
	$page=$in{'page'};	
	if ($page eq "") { $page = 0; }
	$i=0;
	$gentei_log_file = "./member/$in{'ori_ie_id'}/gentei_log.cgi";
	open(IN,"< $gentei_log_file") || &error("Open Error : $gentei_log_file");
	eval{ flock (IN, 1); };
	@bbs_alldata=<IN>;
	foreach (@bbs_alldata){
		($b_num,$b_name,$b_date,$b_title,$b_mail,$b_com,$b_id)= split(/<>/);#koko2006/12/11
		$i++;
		if ($i < $page + 1) { next; }
		if ($i > $page + $gentei_kensuu) { last; }
				print "<div style=\"$gentei_daimei_style\">$b_title</div><div>$b_com�i$b_date�j<span style=\"font-size:9px\">�L��no.$b_num</span></div><br>\n";		#ver.1.40
	}		#foreach��
	close(IN);
	
		$next = $page + $gentei_kensuu;
		$back = $page - $gentei_kensuu;
		print "<div align=center><table border=0><tr>";
		if ($back >= 0) {
			print <<"EOM";
	<td><form method="POST" action="$this_script">
	<input type=hidden name=mode value="houmon">
	<input type=hidden name=con_sele value="3">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=page value="$back">
	<input type=submit value="BACK"></form></td>
EOM
		}
		if ($next < $i) {
			print <<"EOM";
	<td><form method="POST" action="$this_script">
	<input type=hidden name=mode value="houmon">
	<input type=hidden name=con_sele value="3">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=page value="$next">
	<input type=submit value="NEXT"></form></td>
EOM
		}

	print <<"EOM";
	</tr></table></div>
	</td></tr>
	</table>
	<div align=center>
	<form method="POST" action="$this_script">
	<div style=" font-size: 10px; color: #444444"><br>
	<input type=hidden name=mode value="gentei_delete">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	�L��no. <input type=text name=b_num size=8>
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�폜">
	</form>
	���L�����������{�l�ƃQ�[���Ǘ��҂̂݁u�L��no.�v���w�肵�ċL�����폜���邱�Ƃ��ł��܂��B<br>
	</div>
EOM
	&hooter("login_view","�Ƃ��o��");
exit;
}


#�Ǝ�f�����e����
sub gentei_regist {
	&lock;
#���O�t�@�C���X�V
	# ���O��ǂݍ���
	$gentei_log_file = "./member/$in{'iesettei_id'}/gentei_log.cgi";		#ver.1.3
	open(IN,"< $gentei_log_file") || &error("Open Error : $gentei_log_file");
	eval{ flock (IN, 1); };
	# �擪�s���擾
	$top = <IN>;
	local($b_num,$b_name,$b_date,$b_title,$b_mail,$b_com,$b_id)= split(/<>/, $top);#koko2006/12/11
#�^�O�֎~����
#		$in{'b_com'} =~ s/</&lt;/g;
#		$in{'b_com'} =~ s/>/&gt;/g;
	if ($in{'name'} eq $b_name && $in{'b_com'} eq $b_com) {
		&error("��d���e�ł�");
	}
	if ($in{'b_com'} eq "") {
		&error("���e�����͂���Ă��܂���");
	}
	# �V�L��No���擾
	$b_num++;
	# �X�V�z����`
	&time_get;
	$new[0] = "$b_num<>$in{'name'}<>$date2<>$in{'b_title'}<>$in{'b_mail'}<>$in{'b_com'}<>$in{'k_id'}<>\n"; #koko2006/12/11
	$new[1] = $top;

	while (<IN>) {
		$i++;
		push(@new,$_);
		if ($i >= 50){last;}
	}
	close(IN);

# ���O���X�V
	open(OUT,">$gentei_log_file") || &error("Write Error : $gentei_log_file");
	eval{ flock (OUT, 2); };
	print OUT @new;
	close(OUT);
# ���b�N����
	&unlock;
	&message("���e���܂����B","my_house_settei","original_house.cgi");
}

#####���X
sub omise {	
	$omise_log_file = "./member/$in{'ori_ie_id'}/omise_log.cgi";
	open(IN,"< $omise_log_file") || &error("Open Error : $omise_log_file");
	eval{ flock (IN, 1); };
	@omise_alldata=<IN>;
	close(IN);
#koko2007/10/26 �ꏊ�ړ�
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(MK,"< $monokiroku_file") || &error("�����̍w�����t�@�C�����J���܂���");
	eval{ flock (MK, 1); };
	@my_kounyuu_list =<MK>;
	close(MK);
#���L���`�F�b�Nkoko2007/11/04�ꏊ�ړ��ǉ�
	foreach (@my_kounyuu_list){
		&syouhin_sprit ($_);
		if ($syo_kouka eq "�N���W�b�g"){
			if ($syo_taikyuu - (int ((time - $syo_kounyuubi) / (60*60*24)))){
				$siharai_houhou .= "<option value=\"$syo_hinmoku\">$syo_hinmoku</option>";
			}
		}

#koko2007/11/04
		if($kyokahin1 && $syo_hinmoku eq $kyokahin1 || $kyokahin2 && $syo_hinmoku eq $kyokahin2){ #koko2007/10/09
			$kyokasuru = 1;
		}elsif($kyokasuru != 1 && ($kyokahin1 || $kyokahin2)){
			$kyokasuru = 2;
		}
#end2007/11/04
	}

#��ʂŃ\�[�gkoko2006/03/12
#				foreach (@omise_alldata){
#						$data=$_;
#						$key=(split(/<>/,$data))[0];
#						push @tinretu_alldata,$data;
#						push @keys,$key;
#				}
		@tinretu_alldata = @omise_alldata;
		@keys0 = map {(split /<>/)[0]} @tinretu_alldata;
	#	@alldata = @tinretu_alldata[sort {@keys0[$a] cmp @keys0[$b]} 0 .. $#keys0]; #�ύX�~�X
		@tinretu_alldata = @tinretu_alldata[sort {@keys0[$a] cmp @keys0[$b]} 0 .. $#keys0]; #koko2006/08/21

#				sub by_syu_keys{$keys[$a] cmp $keys[$b];}
#				@tinretu_alldata=@tinretu_alldata[ sort by_syu_keys 0..$#tinretu_alldata]; 
#kokoend2006/03/12	
	$omise_settei_file = "./member/$in{'ori_ie_id'}/omise_ini.cgi";
		open(OIB,"< $omise_settei_file") || &error("Open Error : $omise_settei_file");
		eval{ flock (OIB, 1); };
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
#omise_yobi5����{�̔��|�����@omise_yobi6�����i�J�e�S���[�̃X�^�C���ݒ�@omise_yobi7�������N�̃X�^�C��
		close(OIB);
	&ori_header("$omise_body_style","$omise_siasenbako","$omise_yobi7");
		print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM
	print <<"EOM";
	<form method="POST" action="$script">
	<input type=hidden name=mode value="buy_syouhin">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=yakub value="$in{'yakub'}"> <!-- #koko2007/04/27 -->
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center style="$omise_table1_style">
	<tr>
	<td  style="$omise_title_style" nowrap>$omise_title</td>
	<td style="$omise_leed_style" width=65%>$omise_come</td>
	</tr></table><br>
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center style="$omise_table2_style">
	<tr><td colspan=26>�}��F(��)������up�l�A(��)�����wup�l�A(��)������up�l�A(��)���Љ�up�l�A(�p)���p��up�l�A(��)�����yup�l�A(��)�����pup�l�A�i���j=���b�N�Xup�l�A�i�́j=�̗�up�l�A�i���j=���Nup�l�A�i�X�j=�X�s�[�hup�l�A�i�p�j=�p���[up�l�A�i�r�j=�r��up�l�A�i�r�j=�r��up�l�A�iL�j=LOVEup�l�A�i�ʁj=�ʔ���up�l�A�iH�j=�G�b�`up�l<br>
	���M�t�g�͑��蕨��p�̏��i�ł��B�����Ŏg�p���邱�Ƃ͂ł��܂���B
EOM
	if ($kaenai_seigen == 1){		#ver.1.40
		if ($k_id eq "$in{'ori_ie_id'}" || $house_type eq "$in{'ori_ie_id'}"){		#ver.1.3
			print "<br><font color=#ff6600>��������z��҂̂��X�ŏ��i�𔃂����Ƃ͂ł��܂���B</font>";
		}
	}

	print <<"EOM";
	</td></tr>
		<tr style="$omise_koumokumei"><td align=center nowrap>���i</td><td align=center>���i</td><td align=center nowrap>�݌�</td><td>��</td><td>��</td><td>��</td><td>��</td><td>�p</td><td>��</td><td>��</td><td>��</td><td>��</td><td>��</td><td>�X</td><td>�p</td><td>�r</td><td>�r</td><td>L</td><td>��</td><td>�g</td><td align=center nowrap>�J�����[</td><td align=center nowrap>�ϋv</td><td align=center>�g�p<br>�Ԋu</td><td align=center>�g��<br>����</td><td align=center>���]<br>����</td></tr>
EOM

	foreach (@tinretu_alldata) {
			&syouhin_sprit($_);
			if($syo_zaiko <= 0){next;}
#�Ǝ����i�̐ݒ肪����΂��̉��i
			if ($tokubai){
					$syo_nedan = "$tokubai";
			}else{
				if ($omise_syubetu eq "�X�[�p�["){
					$syo_nedan = int($syo_nedan *1.5 * $omise_yobi5);
				}else{
					$syo_nedan = int ($syo_nedan * $omise_yobi5);
				}
			}
			if($syo_zaiko <= 0){
					$kounyuubotan ="";
					$syo_zaiko = "����؂�";
			}else{
					$kounyuubotan ="<input type=radio value=\"$syo_hinmoku,&,$syo_taikyuu,&,$syo_nedan,&,$syo_syubetu,&,\" name=\"syo_hinmoku\">"; #koko2006/08/22
			}
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "�[";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print "<tr style=\"$omise_yobi6\"><td colspan=26>��$syo_syubetu</td></tr>";
			}
			$taikyuu_hyouzi_seikei = "$syo_taikyuu"."$syo_taikyuu_tani";
#ver.1.3��������
if ($syo_nedan =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($syo_nedan) - 3, $j = $syo_nedan =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($syo_nedan, $i, 0) = ',';
  }
}
#ver.1.3�����܂�
#koko2006/11/06 #koko2006/11/07
	if ($syo_comment){
		$disp_seru = "rowspan=\"2\"";
		$disp_com = "<tr><td align=left colspan=24>�y ���l �z $syo_comment</td></tr>"; #koko2006/11/07
	}else{
		$disp_seru = "";
		$disp_com = "";
	}
#koko2007/10/09
		$mottru = 0;#koko2007/10/26
		foreach $tempo(@my_kounyuu_list){
			(@temporari) = split(/<>/,$tempo);
			if($syo_syubetu eq $temporari[0] && $syo_hinmoku eq $temporari[1]){
				if ($temporari[22] eq "��"){
					$keikanissuu = int ((time - $temporari[30]) / (60*60*24));
					$mottru = $temporari[21] - $keikanissuu;
				}else{
					$nokori = int($temporari[21]/$syo_taikyuu);
					if($temporari[21]%$syo_taikyuu){$mottru = $nokori+1;}else{$mottru = $nokori;}
				}
				last;
			}
		}
#koko2007/11/04
		if($kyokasuru == 2 || $kyokasuru == 1){
			$fukyoka = 0;
			foreach $temp0 (@kyokahitsuyou){
				if($syo_hinmoku eq $temp0){
					$fukyoka = 1;
				}
			}
		}

		if($fukyoka == 1 && $mottru && $kyokasuru == 1){
			$in_hinmoku = "$kounyuubotan <font color=\"ff00ff\">$syo_hinmoku($mottru)</font>";
		}elsif($fukyoka == 1 && $mottru){
			$in_hinmoku = "<font color=\"ff00ff\">$syo_hinmoku($mottru)</font>";
		}elsif($fukyoka == 1 && $kyokasuru == 1){
			$in_hinmoku = "$kounyuubotan <font color=\"ff0000\">$syo_hinmoku</font>";
		}elsif($fukyoka == 1){
			$in_hinmoku = "<font color=\"ff0000\">$syo_hinmoku</font>"; #end2007/11/04
		}elsif($mottru){
			$in_hinmoku = "$kounyuubotan <font color=\"0000ff\">$syo_hinmoku($mottru)</font>";
		}else{
			$in_hinmoku = "$kounyuubotan $syo_hinmoku";
		}#end2007/10/26

		print <<"EOM";
		<tr style="$omise_syouhin_table" align=center><td nowrap align=left $disp_seru>$in_hinmoku</td><td align=right nowrap>$syo_nedan�~</td><td align=right>$syo_zaiko</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right nowrap>$calory_hyouzi</td><td nowrap>$taikyuu_hyouzi_seikei</td><td nowrap>$syo_kankaku��</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td></tr>$disp_com
EOM
#kokoend�@end2007/10/26

		$maeno_syo_syubetu = "$syo_syubetu";
	}		#foreach��
#ver.1.30��������
	print <<"EOM";
	<tr><td colspan=26><div align=center>
	�x�������@ <select name="siharaihouhou"><option value="����">����</option>$siharai_houhou</select>
	<input type=submit value=" O K "></div></td></tr>
	</table></form>
	<div align="center"><a href=\"javascript:history.back()\"> [�O�̉�ʂɖ߂�] </a></div>
EOM
#ver1.30�����܂�
	&hooter("login_view","�Ƃ��o��");
	exit;
}


#####�Ǝ�URL
sub dokuzi_url {
	$dokuzi_settei_file = "./member/$in{'ori_ie_id'}/dokuzi_ini.cgi";
		open(OIB,"< $dokuzi_settei_file") || &error("Open Error : $dokuzi_settei_file");
		eval{ flock (OIB, 1); };
			$dokuzi_settei_data = <OIB>;
			($dokuzi_url,$dokuzi_width,$dokuzi_height,$dokuzi_haikei_style,$dokuzi_title,$dokuzi_come,$dokuzi_title_style,$dokuzi_leed_style,$dokuzi_siasenbako,$dokuzi_yobi10) = split(/<>/,$dokuzi_settei_data);
		close(OIB);
	&ori_header("$dokuzi_haikei_style","$dokuzi_siasenbako");
	print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM
	print <<"EOM";
	<table width="$dokuzi_tablewidth" border="0" cellspacing="0" cellpadding="8" align=center style="$dokuzi_table2_style">
	<tr><td>
	<div style = "$dokuzi_title_style">$dokuzi_title</div>
	<div style = "$dokuzi_leed_style">$dokuzi_come</div>
	</td></tr>
	<tr><td align=center>
	<IFRAME src="$dokuzi_url"  width="$dokuzi_width" height="$dokuzi_height" scrolling=auto marginheight=0 FRAMEBORDER=0></IFRAME>
	</td></tr>
	</table></body></html>
EOM
	&hooter("login_view","�Ƃ��o��");
exit;
}

###�����K����������
sub saisensuru {		#ver.1.3
	if ($money < $in{'saisengaku'}){&error("����������܂���B");}
#koko2005/09/01
	if ($in{'saisengaku'} < 0){&error("�}�C�i�X�z�͎�舵���o���܂���B");}
	&osaisen_chc_aite; #koko2005/05/05 �V�K

	$money -= $in{'saisengaku'};
#���O�X�V
	&lock;	
			&temp_routin;
			open(OUT,">$my_log_file") || &error("$my_log_file�ɏ������߂܂���");
			eval{ flock (OUT, 2); };
			print OUT $k_temp;
			close(OUT);

	&openAitelog ($in{'ori_ie_id'});
	$aite_bank += $in{'saisengaku'};
	
			&aite_temp_routin;
				open(OUT,">$aite_log_file") || &error("$aite_log_file���J���܂���");
				eval{ flock (OUT, 2); };
				print OUT $aite_k_temp;
				close(OUT);
#ver.1.40�����܂�
	&aite_kityou_syori("�������K��$name","",$in{'saisengaku'},$aite_bank,"��",$in{'ori_ie_id'},"lock_off");
	&unlock;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
	$aite_name�����$in{'saisengaku'}�~�̂������K�����܂����B
	</td></tr></table>
	<br><br><a href=\"javascript:history.back()\"> [�O�̉�ʂɖ߂�] </a></div>
	</body></html>
EOM
exit;
}

######�ʒ��`�F�b�N koko 2005/05/05
sub osaisen_chc_aite {
	my (@aite_tuutyou);
	$ginkoumeisai_file="./member/$in{'ori_ie_id'}/ginkoumeisai.cgi";
	open(GM,"< $ginkoumeisai_file") || &error("����̗a���ʒ��t�@�C�����J���܂���");
	eval{ flock (GM, 1); };
	@aite_tuutyou = <GM>;
	close(GM);

	&time_get; #$date

	foreach (@aite_tuutyou) {
		my ($tu_date,$meisai,$soukingaku,$nyukigaku) = split(/<>/);
		if ($tu_date eq $date && $meisai eq "�������K��$name"){
			$kojinbetu_osaisen += $nyukigaku;
			if ($kojinbetu_osaisen + $in{'saisengaku'} > $osaisenjyougen){
				&error("�����A���̐l�ւ̂��ΑK������𒴂��܂��B<br>�������K�o���܂���B");
			}

		}
		if ($tu_date eq $date && ($meisai =~ /�������K��./)){
			$total_osaisen += $nyukigaku;
			if ($total_osaisen + $in{'saisengaku'} > $totalosaisenjyougen){
				&error("�����A���̐l�͂��ΑK���\\��������Ă܂��B<br>�������������K���ĂˁB");
			}

		}

	}

}



##########�����̂��X�̏��i���X�g
sub my_syouhin {
	$omise_log_file="./member/$in{'iesettei_id'}/omise_log.cgi";
	open(SP,"< $omise_log_file") || &error("Open Error : $omise_log_file");
	eval{ flock (SP, 1); };
	@myitem_hairetu = <SP>;
	close(SP);
#���i�ύX�̏ꍇ
	if ($in{'command'} eq "���i�ݒ�"){
		if ($in{'syo_nedan'} * 3 < $in{'hanbaikakaku'}){&error("�̔����i�͎d���ꉿ�i�̂R�{�ȓ��ɂ��Ă��������B");}
#		if ($in{'syo_nedan'} / 10 > $in{'hanbaikakaku'}){&error("�̔����i�͎d���ꉿ�i��10����1�ȏ�ɂ��Ă��������B");}
		if($in{'hanbaikakaku'} =~ /[^0-9]/){&error("�̔����i���s�K�؂ł��B");}			#ver.1.3
		@new_myitem_hairetu =(); #koko2007/06/05
		foreach  (@myitem_hairetu) {
			&syouhin_sprit($_);
			if ($in{'syo_hinmoku'} eq "$syo_hinmoku"){
					$tokubai = $in{'hanbaikakaku'};
					$syo_comment = $in{'bikou'}; #koko2007/09/27
			}
			&syouhin_temp;
			push (@new_myitem_hairetu,$syo_temp);
		}
		&lock;
		open(OUT,">$omise_log_file") || &error("Write Error : $omise_log_file");
		eval{ flock (OUT, 2); };
		print OUT @new_myitem_hairetu;
		close(OUT);	
		&unlock;
		&message("$in{'syo_hinmoku'} �̉��i��$in{'hanbaikakaku'}�~�ɐݒ肵�܂����B<br>���l���u$in{'bikou'}�v�ɂ��܂����B","my_syouhin","original_house.cgi");#koko2007/09/27
	}
	
#��ʂŃ\�[�g
#koko2006/03/12
				@alldata = @myitem_hairetu;
#				foreach (@myitem_hairetu){
#						$data=$_;
#						$key=(split(/<>/,$data))[0];
#						push @alldata,$data;
#						push @keys,$key;
#				}

				@keys0 = map {(split /<>/)[0]} @myitem_hairetu;
				@alldata = @alldata[sort {@keys0[$a] cmp @keys0[$b]} 0 .. $#keys0];


#				sub by_syu_keys{$keys[$a] cmp $keys[$b];}
#				@alldata=@alldata[ sort by_syu_keys 0..$#alldata]; 
#kokomade

#���X�ݒ�t�@�C�����̔��|�������擾
	$omise_settei_file = "./member/$in{'iesettei_id'}/omise_ini.cgi";
		open(OIB,"< $omise_settei_file") || &error("Open Error : $omise_settei_file");
		eval{ flock (OIB, 1); };
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
		close(OIB);
		
	&header(omise_list_style);
	print <<"EOM";
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>�e���i�̔̔����i�͂�����Ōʂɐݒ肷�邱�Ƃ��ł��܂��B�������A�d���ꉿ�i�̂R�{�ȏ�ɐݒ肷�邱�Ƃ͂ł��܂���B<br>
	���݂̂��X�̎�� = $omise_syubetu</td>
	</tr></table><br>
	
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center class=yosumi>
	<tr><td colspan=28><font color=#330033>�}��F(��)������up�l�A(��)�����wup�l�A(��)������up�l�A(��)���Љ�up�l�A(�p)���p��up�l�A(��)�����yup�l�A(��)�����pup�l�A�i���j=���b�N�Xup�l�A�i�́j=�̗�up�l�A�i���j=���Nup�l�A�i�X�j=�X�s�[�hup�l�A�i�p�j=�p���[up�l�A�i�r�j=�r��up�l�A�i�r�j=�r��up�l�A�iL�j=LOVEup�l�A�i�ʁj=�ʔ���up�l�A�iH�j=�G�b�`up�l<br>
	���ϋv�́A����Ȃ�g�p�ł���񐔁A�����Ȃ�g�p�ł�������ł��B<br>
	���J�����[�͐ێ�ł��鐔�l�ł��B</font></td></tr>
		<tr bgcolor=#996699><td align=center nowrap>���i</td><td align=center nowrap>�̔����i</td><td align=center nowrap>�d���ꉿ�i</td><td align=center nowrap>�݌�</td><td>��</td><td>��</td><td>��</td><td>��</td><td>�p</td><td>��</td><td>��</td><td>��</td><td>��</td><td>��</td><td>�X</td><td>�p</td><td>�r</td><td>�r</td><td>L</td><td>��</td><td>�g</td><td align=center nowrap>�J�����[</td><td align=center>�g�p<br>�Ԋu</td><td align=center nowrap>�g��<br>����</td><td align=center nowrap>���]<br>����</td><td align=center nowrap>�ϋv</td><td align=center nowrap>�w����</td></tr>
EOM

	foreach (@alldata) {
			&syouhin_sprit($_);
			if ($omise_syubetu ne "�X�[�p�["){
				if ($omise_syubetu ne "$syo_syubetu"){next;}
			}
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "<div align=center>�[</div>";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print "<tr bgcolor=#cc9999><td colspan=28>��$syo_syubetu</td></tr>";
			}
			$taikyuu_hyouzi_seikei = "$syo_taikyuu"."$syo_taikyuu_tani";
			&byou_hiduke($syo_kounyuubi);
			if ($omise_syubetu eq "�X�[�p�["){
				$syo_nedan *= 1.5;
			}
#�Ǝ��̉��i�ݒ�����Ă���ꍇ���̉��i�A�����łȂ���ΐݒ�̊|����
			if ($tokubai){$hannbaityuu = "$tokubai";}else{$hannbaityuu = $syo_nedan * $omise_yobi5;}

		print <<"EOM"; #koko2007/09/27
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="my_syouhin">
	<input type=hidden name=command value="���i�ݒ�">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=hidden name=syo_hinmoku value="$syo_hinmoku">
	<input type=hidden name=syo_nedan value="$syo_nedan">
		<tr bgcolor=#ffcccc align=center><td nowrap align=left>$syo_hinmoku<input type=submit value="OK"></td><td nowrap><input type="text" name="hanbaikakaku" size=8 value=$hannbaityuu><td nowrap align=right>$syo_nedan</td></td><td nowrap>$syo_zaiko</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right>$calory_hyouzi</td><td nowrap>$syo_kankaku��</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td><td nowrap>$taikyuu_hyouzi_seikei</td><td nowrap>$bh_tukihi</td></tr><tr bgcolor=#cccccc><td align=left colspan=27><input type="text" name="bikou" size=80 value=$syo_comment>$syo_comment<br></td></form></tr>
EOM
		$maeno_syo_syubetu = "$syo_syubetu";
	}		#foreach��
	if (! @alldata){print "<tr><td colspan=26>���ݏ��L���Ă���A�C�e���͂���܂���B</td></tr>";}
	print <<"EOM";
	</table>
EOM
	&hooter("my_house_settei","�߂�","original_house.cgi");
	exit;
}

###BBS�L���폜
sub bbs_delete {
	if ($in{'b_count'} eq "" && $in{'oya_count'} eq "" && !$in{'all_del'}){&error("�L��no.���w�肳��Ă��܂���");} #koko2007/09/17
	&lock;
#���O�t�@�C���X�V
	# ���O��ǂݍ���
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_log_file = "./member/admin/bbs".$in{'bbs_num'}."_log.cgi";
	}else{
		$bbs1_log_file = "./member/$in{'ori_ie_id'}/bbs1_log.cgi";
	}
	open(IN,"< $bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	eval{ flock (IN, 1); };
	$count_gyou = <IN>;
	@all_data = <IN>;
	close(IN);
	$kizi_atta_flag = 0;
	$sakujo_b_num = "";
	@new_all_data = ();
	$i=0;
	foreach $tep_dat(@all_data){
		($b_num,$b_name,$b_date,$b_res,$b_mail,$b_com,$b_id)= split(/<>/, $tep_dat);#koko2006/12/11
		if ($in{'b_count'} eq "$b_mail"){
			$kizi_atta_flag = 1;
			if ($b_num){$sakujo_b_num = "$b_num";}else{$sakujo_b_num = "res";}
			$b_name =~ s/<span style="font-size:9px">�i.*//;
			if (!($in{'name'} eq $admin_name || $in{'ori_ie_id'} eq $k_id)){ #koko2006/11/25
				&error("�Ǘ��҈ȊO�͋L���폜�ł��܂���B");
			}else{
				$tep_dat = "";#koko2007/04/19
				next;
			}
		}

#koko2007/09/17
		if (!($in{'name'} eq $admin_name || $in{'ori_ie_id'} eq $k_id)){ #koko2006/11/25
			&error("�Ǘ��҈ȊO�͋L���폜�ł��܂���B");
		}else{
			if ($in{'oya_count'}){
				if($delettyu && $b_num){
					$delettyu = 0;
				}
				if($b_num eq $in{'oya_count'}){
					$kizi_atta_flag = 1;
					$delettyu = 1;
					next;
				}
			}
		}
#kokoend


		if ($b_res){if ($b_res eq "$sakujo_b_num"){&error("�q�L���̂����e�L���͍폜�ł��܂���B");}}
	#	$bbs_temp = "$b_num<>$b_name<>$b_date<>$b_res<>$b_mail<>$b_com<>$b_id<>\n"; #koko2006/12/14

		push (@new_all_data,$tep_dat);#koko2007/04/19
	#	push (@new_all_data,$bbs_temp);
	}
#koko2007/09/17
	if (!($in{'name'} eq $admin_name || $in{'ori_ie_id'} eq $k_id)){ #koko2006/11/25
		&error("�Ǘ��҈ȊO�͋L���폜�ł��܂���B");
	}else{
		if ($in{'all_del'}){
			$kizi_atta_flag = 1;
			@new_all_data = ();
		}
	}
	if ($kizi_atta_flag == 0){&error("�Y������L��no.��������܂���B");}
#	unshift (@new_all_data,$count_gyou);
	open (OUT,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
	eval{ flock (OUT, 2); };
	print OUT $count_gyou;#koko2007/04/19
	print OUT @new_all_data;
	close(OUT);
	&unlock;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">�L�����폜���܂����B1</span>
</td></tr></table>
<br>
	<form method=POST action="$this_script">
EOM
	if ($in{'ori_ie_id'} eq "admin"){
		print "<input type=hidden name=mode value=\"normal_bbs\">";
	}else{
		print "<input type=hidden name=mode value=\"houmon\">";
	}
	print <<"EOM";
	<input type=hidden name=con_sele value="0">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>
EOM
	exit;
}

###�Ǝ����f���L���폜
sub gentei_delete {
	if ($in{'ori_ie_id'} != $k_id and $in{'ori_ie_id'} != $house_type and $in{'name'} ne $admin_name){&error("�Ǝ�i�z��ҁj�A�Q�[���Ǘ��҈ȊO�͋L���폜�ł��܂���B");}
	if ($in{'b_num'} eq ""){&error("�L��no.���w�肳��Ă��܂���");}
	&lock;
#���O�t�@�C���X�V
	# ���O��ǂݍ���
	$gentei_log_file = "./member/$in{'ori_ie_id'}/gentei_log.cgi";
	open(IN,"< $gentei_log_file") || &error("Open Error : $gentei_log_file");
	eval{ flock (IN, 1); };
	@all_data=<IN>;
	close(IN);
	$kizi_atta_flag = 0;
	@new_all_data = ();
	foreach $tep_dat(@all_data){
		($b_num,$b_name,$b_date,$b_title,$b_mail,$b_com,$b_id)= split(/<>/, $tep_dat);#koko2006/12/11
		if ($in{'b_num'} eq "$b_num"){
			$kizi_atta_flag = 1;
			if ($name ne $b_name &&  $in{'name'} ne $admin_name){&error("�������{�l�ȊO�͋L���폜�ł��܂���B");
			}else{
				$tep_dat = "";#koko2007/04/19
				next;
			}
		}
	#	$bbs_temp = "$b_num<>$b_name<>$b_date<>$b_title<>$b_mail<>$b_com<>$in{'k_id'}<>\n"; #koko2006/12/11
		push (@new_all_data,$tep_dat);#koko2007/04/19
	#	push (@new_all_data,$bbs_temp);
	}
	if ($kizi_atta_flag == 0){&error("�Y������L��no.��������܂���B");}
	open (OUT,">$gentei_log_file") || &error("Write Error : $gentei_log_file");
	eval{ flock (OUT, 2); };
	print OUT @new_all_data;
	close(OUT);
	&unlock;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">�L�����폜���܂����B2</span>
</td></tr></table>
<br>
	<form method=POST action="$this_script">
	<input type=hidden name=mode value="houmon">
	<input type=hidden name=con_sele value="3">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=submit value="�߂�">
	</form></div>
EOM
	exit;
}