#!/usr/local/bin/perl

# �����g���̃T�[�o�[�̃p�X�ɍ��킹�Ă��������B#2006/10/20 OUT 
#+++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2003-2004 brassiere
$version = 'TOWN ver.1.40';
#  web�Fhttp://brassiere.jp/
#  mail�Fshohei@brassiere.jp
#���̃v���O�����ɂ���ċN�������ɐӔC�𕉂��܂���B
#+++++++++++++++++++++++++++++++++++++

#�@�����̃v���O�����̓t���[�E�G�A�ł����A�Q�[�����Ŏ��X�u�e�L�X�g�L���v���\������܂��B�܂��A�\�z�ȏ�ɘJ�͂Ǝ��Ԃ��������Ă��܂������߁A�C�ӂ̎g�p�����̂��x���������}���Ă��܂��B���ۂɐݒu���A�^�p������ŗ������x���������̉��l������Ǝv��ꂽ���́A�K���Ǝv����z���x�����Ă���������ƂƂĂ��������ł��B����̊J�����ێ����Ă������߂ɉ�������������Ɣ��ɏ�����܂�
#	  �������x�����`���͂���܂��񂵁A�@�\����������܂���B�܂��������x�����Ă������������Ƃ����łȂ����ŋ�ʂ��邱�Ƃ͂���܂���B�x����Ȃ��̂����ʂ��Ǝv���Ă܂��̂ŁA���ނ��Ƃ�����܂���i�΁B����ł��������x�����ĉ�����Ƃ������́A���L�U����܂ő��������肢�������܂��B

#�@���C�ӂ̗����x���恄
#�@�݂��ً�s�@�W�����x�X�@���ʗa��
#�@�x�X�ԍ��F822
#�@�����ԍ��F9502477
#�@���l���F�C�[�o���N�M���R�E(�J

#�@�������̖ڈ��i�����܂ŎQ�l�ŁA����ȉ��ł�����ȏ�ł��\���܂��񂗁j
#�@������������500�~
#�@�����̂���������������1000�~
#�@�����������I�f���炵���I��1500�~

#�@���d�v���@���̃Q�[���͉摜�ʐς��傫���A����ɕp�ɂɓǂݍ��݂����邽�߁A���Ƀg���t�B�b�N�e�ʂɂ����Ē��ӂ�v���܂��i���T�C�g�ł̉ғ����тł͂܂�������������Ȃ��ꍇ�A10����10�f���̃g���t�B�b�N�ʂƂȂ��Ă��܂��j�B�ݒu�̍ۂ͂��̃T�[�o�[�Œ�߂�ꂽ�g���t�B�b�N�e�ʂ��m�F������Łu�X�̈ړ����ԁv����сu�s���̐������ԁv���Ȃ�ׂ��������A��Ƀg���t�B�b�N�ʂ̐��ڂ��`�F�b�N���邱�Ƃ����������߂��܂��B�܂��A�T�[�o�[�𕡐��������ł���Ή摜�̂ݕʃT�[�o�[�ɒu���i�����ݒ�ŉ摜�t�H���_�[�̎w�������j�A�g���t�B�b�N�ʂ𕪎U�����邱�Ƃ��L���ł��B
# �����_���Љ�ҏ��� #'yes';'no';'';�̎O��� #1/2 game.cgi �ɂ�����B
$syokai = 'no';#""; 

# �A�C�e���̐���\�� koko2007/04/28
$kazu_disp = 'yes';
# �^�E���i���o�[�̕ۑ� 2007/09/18
$hozontown = 'yes';

# �v���_�E���^�E���y�[�W"no","yes","yes2","yes3":
$dairekutoin = 'yes3';
# eval{ flock (IN, 2); }; ���b�N���� koko2007/06/18 sleep
###############################################################

require './jcode.pl';
require './cgi-lib.pl';
require './top.pl';
require './town_ini.cgi';
require './command.pl';
require './event.pl';
require './town_lib.pl';		#ver.1.4
require './unit.pl';		#ver.1.4
&decode;

# �w��z�X�g�A�N�Z�X����
	# �z�X�g�����擾
	$get_host = $ENV{'REMOTE_HOST'}; #2007/05/16
#	if (!$get_host){$get_host = $ENV{'REMOTE_ADDR'};} #2007/05/16
	$get_addr = $ENV{'REMOTE_ADDR'};
	if ($get_host eq "" || $get_host eq $get_addr) {
		$get_host = gethostbyaddr(pack("C4", split(/\./, $get_addr)), 2) || $get_addr;
	}
if ($get_host eq "") { &error("�������܂����z�X�g���擾�ł��Ȃ����ł̓A�N�Z�X�ł��܂���"); }
#koko2007/10/10
if ($host_kyuka_meker eq 'yes'){
	if($okhost){
		local($flag)=1;
		foreach ( split(/\s+/, $okhost) ) {
			s/(\W)/\\$1/g;
			s/\*/\.\*/g;
			if ($get_host =~ /$_/) { $flag=0; last; }
		}
		if ($flag) { 
			$admin_pass = ''; 
		}
	}else{
		($host1,$host2,$host3,$host4) = split(/\./, $get_host);
		if ($host1 !~ /\D/ && $host2 !~ /\D/ && $host3 !~ /\D/ && $host4 !~ /\D/){&error("host error $get_host");} #2007/10/10

		(@host5) = split(/\./, $get_host);
		$i = 0;
		foreach (@host5){
			if ($_ eq 'jp' || $_ eq 'JP' || $_ eq 'net'){
				$i++;
				if ($i >= 2){&error("host error $get_host");} #2007/10/10
			}
		}

#		$get_host = "'*'.$host5[1].$host5[2].$host5[3].$host5[4].$host5[5].$host5[6].$host5[7]"; # *.123,abc.ne.jp �擪�����u*�v�L��

		(@kanri1) = split(/\./, $my_host1);
		if ($kanri1[0] eq '*'){
			$oboegaki1 = $host5[0];
			$host5[0] ='*';
			$get_host1 = join(".",@host5);
		}else{$get_host1 = $get_host;}
		$itti = "1";
		if ($my_host1 && $my_host1 eq $get_host1){ #
			$itti = "yes";
		}elsif($my_host1){$itti = "no";}
		if($oboegaki1){$host5[0] = $oboegaki1;}
		$get_host = join(".",@host5);
		(@kanri2) = split(/\./, $my_host2);
		if ($kanri2[0] eq '*'){
			$oboegaki2 = $host5[0];
			$host5[0] ='*';
			$get_host2 = join(".",@host5);
		}else{$get_host2 = $get_host;}
		if ($my_host2 && $my_host2 eq $get_host2 && ($itti eq "no" || $itti eq "1")){
			$itti = "yes";
		}elsif($my_host2){$itti = "no";}
		if ($itti eq "no"){
			$admin_pass = '';
		}
		if($oboegaki2){$host5[0] = $oboegaki2;}
		$get_host = join(".",@host5);
	}
}
#kokoend #koko2007/04/17
	open(IN,"< dene2.cgi") || &error("Open Error : dene2.cgi");
	eval{ flock (IN, 1); };
	@dene2 = <IN>;
	close(IN);
	@deny = (@deny,@dene2);
#kokoend2007/04/17
	foreach (@deny) {
		if ($_ eq "") { next; }
		chomp $_;
		$_ =~ s/\*/\.\*/g;
		if ($get_host =~ /$_/i) { &error("�������܂��������p���̃z�X�g����̓A�N�Z�X�ł��܂���"); }
	}
#kokoend
	
#�����e�`�F�b�N
	if($mente_flag == 1 && $in{'admin_pass'} eq "" && $in{'mode'} ne ""){&error("$mente_message")}	#ver.1.2

sub joukenbunki {
}

$seigenyou_now_time = time;
#�������ԃ`�F�b�N
		$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $access_byou);
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("�܂��s���ł��܂���B����$ato_nanbyou�b���҂����������B")}

#ver.1.40��������
#�p�X���[�h���O�쐬
	if ( !-e $pass_logfile){
		open(LOGF,"< $logfile") || &error("Open Error : $logfile");
		eval{ flock (LOGF, 1); };
		@pass_sakuse = <LOGF>;
		close(LOGF);
		@henkan_pass = (); #koko2007/07/21
		foreach (@pass_sakuse){
			&list_sprit($_);
			$henkan_temp = "$list_k_id<>$list_name<>$list_pass<>\n";
			push (@henkan_pass,$henkan_temp);
		}

#		sub by_r_number {$b <=> $a;}
#		@henkan_pass = sort by_r_number @henkan_pass;
#koko2005/10/08
	@henkan_pass = sort {$b <=> $a} @henkan_pass;
#kokoend


		open(PSS,">$pass_logfile") || &error("Write Error : $pass_logfile");
		eval{ flock (PSS, 2); };
		print PSS @henkan_pass;
		chmod 0666,"$pass_logfile";
		close(PSS);
	}
#koko2007/02/10
	if ($in{'mode'} eq "shiharaihouhou"){
		$shiharai = $in{'shiharai'};
		$in{'mode'} = "login_view";
	}
#kokoend
#��������
	if($in{'mode'} eq "login_view"){&login_view;}
	if($in{'mode'} eq "orosi"){&orosi;}
	if($in{'mode'} eq "buy_orosi"){&buy_orosi;}
	if($in{'mode'} eq "gym"){&gym;}
	if($in{'mode'} eq "training"){&training;}
	if($in{'mode'} eq "syokudou"){&syokudou;}
	if($in{'mode'} eq "syokuzisuru"){&syokuzisuru;}
	if($in{'mode'} eq "syokudou2"){&syokudou2;}		#koko2006/07/16
	if($in{'mode'} eq "syokuzisuru2"){&syokuzisuru2;}	#koko2006/07/16
	if($in{'mode'} eq "school"){&school;}
	if($in{'mode'} eq "do_school"){&do_school;}
	if($in{'mode'} eq "depart_gamen"){&depart_gamen;}
	if($in{'mode'} eq "depart_gamen2"){&depart_gamen2;}	#koko2006/11/20
	if($in{'mode'} eq "buy_syouhin"){&buy_syouhin;}
	if($in{'mode'} eq "buy_syouhin2"){&buy_syouhin2;}	#koko2006/11/20
	if($in{'mode'} eq "hanbai"){&hanbai;}			#koko2006/11/28
	if($in{'mode'} eq "buy_syouhin_hanbai"){&buy_syouhin_hanbai;} #koko2006/11/28
	if($in{'mode'} eq "kentiku"){&kentiku;}
	if($in{'mode'} eq "kentiku_do"){&kentiku_do;}
	if($in{'mode'} eq "aisatu"){&aisatu;}
	if($in{'mode'} eq "mail_sousin"){&mail_sousin;}
	if($in{'mode'} eq "mail_do"){&mail_do;}
#	if($in{'mode'} eq "jamp_url"){&jamp_url;} #2007/09/26
#ver.1.40�����܂�
	&main_view($in{'town_no'});
exit;


###################�T�u���[�`��

#���O�C�����
sub login_view {
#���t�����ς���Ă����ꍇ�̃C�x���g
	&time_get;
	my ($hutuu_risoku,$teiki_risoku);
	if ($access_time ne "$date"){
		$access_time = $date;
#�a���̗����v�Z
		$hutuu_risoku = int ($bank*0.005);
		if ($hutuu_risoku > 0){
			$bank += $hutuu_risoku;
			&kityou_syori("���ʗa������","",$hutuu_risoku,$bank,"��");
		}
		$teiki_risoku = int ($super_teiki*0.01);
		if ($teiki_risoku > 0){
			$super_teiki += $teiki_risoku;
			&kityou_syori("�X�[�p�[�������","",$teiki_risoku,$super_teiki,"��");
		}
#�Z��[���������Ƃ�
		if ($loan_kaisuu > 0){
			$bank -= $loan_nitigaku;
			$loan_kaisuu --;
			&kityou_syori("�Z��[���x����","$loan_nitigaku","",$bank,"��");
		}
#�q������̎d���菈��
		&kodomo_siokuri;
	#	&unei_siokuri; #koko2007/04/17
		&unei_siokuri2; #koko2007/04/29 &unei_siokuri�Ƃǂ��炩���g���B
		&unei_siokuri3; #koko2007/05/26
	}
#���̂������ꍇ
	if ($in{'ziko_flag'} eq "on" && $in{'ziko_idousyudan'} ne "�k��"){
		$monokiroku_file="./member/$k_id/mono.cgi";
		open(OUT,"< $monokiroku_file") || &error("Open Error : $monokiroku_file");
		eval{ flock (OUT, 1); };
		@mycar_hairetu = <OUT>;
		close(OUT);
		$ziko_sya_flg=0;
#ver.1.40��������
		@new_mycar_hairetu =(); #koko2007/06/05
		foreach  (@mycar_hairetu) {
			&syouhin_sprit($_);
#koko2006/12/31
			if ($syo_syubetu ne  "�M�t�g" && $syo_taikyuu > 0 && $in{'ziko_idousyudan'} eq "$syo_hinmoku" && $ziko_sya_flg == 0){
				$syo_taikyuu -- ;
				$ziko_sya_flg=1;
				if ($syo_taikyuu <= 0){
					$taiha_comment = "$in{'ziko_idousyudan'}�͑�j���܂����B";
				}else{
					$taiha_comment = "�c��̑ϋv�i$syo_taikyuu�j";
				}
#ver.1.40�����܂� #koko2006/12/31
			}
			&syouhin_temp;
			push (@new_mycar_hairetu,$syo_temp);
		}
#�����̏��L���t�@�C�����X�V
		&lock;
		open(OUT,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
		eval{ flock (OUT, 2); };
		print OUT @new_mycar_hairetu;
		close(OUT);
#koko2006/11/27
		$loop_count = 0;
		while ($loop_count <= 10){
			for (0..50){$i=0;}
			@f_stat_b = stat($monokiroku_file);
			$size_f = $f_stat_b[7];
			if ($size_f == 0 && @new_mycar_hairetu ne ""){
			#	sleep(1);#2006/11/27#koko2007/02/02
				open (OUT, "> $monokiroku_file") or &error("�G���[�E�t�@�C�����J���܂��� $monokiroku_file");
				eval{ flock (OUT, 2); };
				print OUT @new_mycar_hairetu;
				close (OUT);
			}else{
				last;
			}
			$loop_count++;
		}
#kokoend#koko2007/01/21
	if ($in{'maigo'} eq 'yes'){
		$in{'town_no'} = 3;
		$disp = "<br>���܂��ɖ��q�ɂȂ��Ă��܂��܂����B<br>$town_hairetu[$in{'town_no'}]�ɍs���Ă��܂��܂����B";
	}
	&unlock;
	&message("<font color=#ff6600>��ʎ��̂��N�����Ă��܂��܂����I<br>�u$in{'ziko_idousyudan'}�v�̑ϋv�x���P����܂��B<br>$taiha_comment$disp</font>","login_view");
	}		#���̂������ꍇ��
	#���q�@
	if ($in{'maigo'} eq 'yes'){
		$in{'town_no'} = 3;
		&message("<font color=#ff6600>���q�ɂȂ�܂����B<br>$town_hairetu[$in{'town_no'}]�ɍs���Ă��܂��܂����B</font>","login_view");
	} #kokoend

	&event_happen;
	$k_sousisan = $money + $bank + $super_teiki - ($loan_nitigaku * $loan_kaisuu);
	&main_view("$in{'town_no'}");
exit;
}

#�g�b�v��ʉE����
sub top_gamen {
	open(IN,"< $maintown_logfile") || &error("Open Error : $maintown_logfile");
	eval{ flock (IN, 1); };
			$maintown_para = <IN>;
			if ($maintown_para eq ""){&error("$maintown_logfile�ɖ�肪����܂��B���萔�ł����Ǘ��l�i$master_ad�j�܂ł��A�����������B");}			#�󃍃O�`�F�b�N		ver.1.22
			&main_town_sprit($maintown_para);
	close(IN);
	&time_get;
#���t���ς���Ă����烁�C���^�E�����O�������̓��t�ɍX�V�A�������A�����̉��������X�V�A���t���O�ƐH���t���O��0�ɂ���
	if($date ne $mt_today){
			$mt_today=$date;
			$mt_t_time=$mt_y_time;
			$mt_y_time=int(rand(20))+1;		#ver.1.3
			$mt_orosiflag=0;
			$mt_syokudouflag=0;
			$mt_departflag=0;
			&main_town_temp;
			&lock;
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			eval{ flock (OUT, 2); };
			print OUT $mt_temp;
			close(OUT);	
			&list_log_backup;
			&unlock;
	}

	open(IN,"< $logfile") || &error("Open Error : $logfile");
	eval{ flock (IN, 1); };
	@rankingMember = <IN>;
	$sankasyasuu = @rankingMember;
	close(IN);
	my $mt_keizai_hyouzi = int ($mt_keizai / (int(($date_sec - $mt_yobi8)/(60*60*24))+1));
	my $mt_henei_hyouzi = int ($mt_hanei / (int(($date_sec - $mt_yobi8)/(60*60*24))+1));
			if ($tajuukinsi_flag==1){$tajuucomment = "<br>�����d�o�^�͋֎~�ł��B";}
			if ($tajuukinsi_deny==1){$tajuucomment .= "���d�o�^�����o�������_�Ń��O�C���ł��Ȃ��Ȃ�܂��̂ł����ӂ��������B";}
 # %machi_gazou=('���������^�E��','./img/keiba_tytle.gif','�V�[���]�[�g','./img/kentiku_tytle.gif');
	print <<"EOM";
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td>
           <div align="center"><font size="5"><b>$title</b></font></div>
	   <!-- <div align="center"><img src="$machi_gazou{"$title"}" alt="$title"></div>> -->
          </td>
        </tr>
        <tr><td  class="theue"><img src="$img_dir/dat.gif" alt="�f�[�^"></td></tr><tr>
          <td  class="thanaka" background="$img_dir/townnameback.gif">
<span  onMouseOver='onMes5(\"�o�^����Ă��郆�[�U���i�X�S�́j\")' onMouseOut='onMes5(\"\")'>�l���F$sankasyasuu�l</span>�@<span  onMouseOver='onMes5(\"�Z���̂��X�̕��ςP������グ�z�i�X�S�́j\")' onMouseOut='onMes5(\"\")'>�o�ϗ́F$mt_keizai_hyouzi�~</span>�@<span  onMouseOver='onMes5(\"�f���̕��ςP���������ݐ��i�X�S�́j\")' onMouseOut='onMes5(\"\")'>�ɉh�x�F$mt_henei_hyouzi</span></td></tr><tr>
<td  class="thanaka"><img src="$img_dir/tod.gif" alt="�����́E�E�E�B"></td></tr><tr><td  class="theshita" background="$img_dir/townnameback.gif">
$top_nannichi</td>
        </tr>
        <tr>
          <td>	$osirase
<!-- ver.1.30�������� --> 
EOM
#koko2006/11/29
if ($genzaino_ninzuu >= $douzi_login_ninzuu){
	print <<"EOM";
		<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>���݁A�������O�C������$douzi_login_ninzuu�l�𒴂��Ă��܂��B�������܂����A���΂炭���Ă��烍�O�C�����Ă��������B</td></tr></table>
EOM
	}else{
#koko2007/09/26
		if($hozontown eq 'yes'){$disp_tag = "<input type=\"hidden\" name=\"town_no\" value=\"$ck{'town_no'}\">\n";}else{$disp_tag="";}
		if ($dairekutoin eq 'yes' || $dairekutoin eq 'yes3'){
			$disp_tag = "�X��I�� �F <select name=\"town_no\">\n";
			$disp_tag .= "<option value=\"\">����</option>\n";
			if($hozontown eq 'yes'){$disp_tag .= "<option value=\"$ck{'town_no'}\">�L��</option>\n";} 
			$i=0;
			foreach (@town_hairetu){
				if($machikakushi eq 'yes'){ #koko2007/10/21
					if($_ eq $kakushimachi_name && $kakushimachi_name || $_ eq $kakushimachi_name1 && $kakushimachi_name1 || $_ eq $kakushimachi_name2 && $kakushimachi_name2 || $_ eq $kakushimachi_name3 && $kakushimachi_name3 || $_ eq $kakushimachi_name4 && $kakushimachi_name4){
						$i++;
						next;
					}
				}
				$disp_tag .= "<option value=\"$i\">$_</option>\n";
				$i++
			}
			$disp_tag .= "</select><br>\n";
		}
#koko2006/11/29
		print <<"EOM";
<Script Language="JavaScript">
<!--
function bzc(){
	document.getoin.burauza_in.value = navigator.appName;
}
//-->
</Script>
	<form method="POST" name="getoin" action="$script">
	<input type=hidden name="mode" value="login_view">
	<input type="hidden" name="burauza_in" value="">
        �����O�C���i�o�^�ς݂̕��j<br>
        ���@���@�O �F 
        <input type="text" name="name" size="18" value="$ck{'name'}" maxlength="16"><br>
        �p�X���[�h �F 
        <input type="password" name="pass" size="18" value="$ck{'pass'}" maxlength="10"><br>
	$disp_tag<br>
EOM
	if ($sanka_hyouzi_kinou == 1){
		print <<"EOM";
		�Q���҈ꗗ�ɖ��O�� <input type="radio" name="sanka_hyouzi_on" value="off"> �\\�������Ȃ� 
		<input type="radio" name="sanka_hyouzi_on" value="on" checked>  �\\��������<br>
EOM
	}
		print <<"EOM"; #koko2007/01/18
        <div align=center><input type="submit" value="OK" onMouseDown='bzc()'></div>
      </form>
	<hr size=1>
EOM
#kokoend
	if ($sankasyasuu >= $saidai_ninzuu){
		print "�����݁A�ő�o�^�l���ɒB���Ă��܂��̂ŐV�K�o�^�͂ł��܂���B";
	}elsif($new_touroku_per == 1) {
		print "�����݁A�V�K�o�^�𒆎~���Ă��܂��B";
	}else{
#koko2007/09/13
		if ($syokai ne 'no'){
			$disp_syukai = "�Љ�R�[�h�F <input type=\"text\" name=\"syokai\" size=\"18\" maxlength=\"16\"><br>\n";
		}else{$disp_syukai = "";}
#kokoend
		print <<"EOM";
     <form method="POST" action="game.cgi">
	<input type=hidden name=mode value="new">
		���V�K�o�^�i�ő�o�^�l���F$saidai_ninzuu�l�j$tajuucomment<br>
        ���@���@�O�F 
        <input type="text" name="name" size="18" maxlength="16"><br>
<!-- #koko2007/09/13 -->
	$disp_syukai
<!-- #kokomade2007/09/13 -->
        �p�X���[�h�F 
        <input type="password" name="pass" size="18" maxlength="10"><br>
		���@�@�@�ʁF 
        <input type="radio" name="sex" value="m">�j 
		<input type="radio" name="sex" value="f">��<br>
        <div align=center><input type="submit" value="OK"></div>
      </form>
<hr>
���uCustomer Floor�v�Ƀ��O�C���i��A�̕��j
<FORM ACTION="password.cgi" METHOD="post">
<TABLE border="1">
  <TBODY>
    <TR>
      <TD align="right"><BR>
      ���[�U�[ID</TD>
      <TD><INPUT type="text" name="id"></TD>
    </TR>
    <TR>
      <TD align="right">�p�X���[�h</TD>
      <TD><INPUT type="password" name="pass"></TD>
    </TR>
    <TR>
      <TD colspan="2" align="center"><INPUT TYPE="SUBMIT" VALUE="���M">
<INPUT TYPE="RESET" VALUE="�N���A"></TD>
    </TR>
  </TBODY>
</TABLE>
</FORM>
<HR>
�Z�p�񋟁F<A href="http://cgi-garage.parallel.jp/">CGI-Garage</A>
<HR>
EOM
	}
}		#�����l���𒴂��Ă��Ȃ��ꍇ�̕�
# ver.1.30�����܂�
	print <<"EOM";
<!-- koko2006/12/27-->
	<hr size=1>
	<form method=POST action="admin2.cgi">
	<input type=hidden name=mode value="admin">
	<input type=hidden name=name value="$ck{'name'}">
	<input type=hidden name=kanri value="fuku">
	�p�X���[�h <input type=password size=8 name="admin_pass"> <input type=submit value="���Ǘ��҃��j���[">
	</form>
<!-- koko2006/12/27-->
	<hr size=1>
	<form method=POST action="admin.cgi">
	<input type=hidden name=mode value="admin">
	�Ǘ��҂h�c <input type="text" size=10 name="kanrisya_id"><br><!-- koko2005/10/07-->
	�p�X���[�h <input type=password size=8 name="admin_pass"> <input type=submit value="�Ǘ��҃��j���[">
	</form>
		  </td>
        </tr>
      </table>
EOM
}

#�X��񑋂̏o�́@�����܂Ղ� 2008/03/25�@����ɉ���2009/02/07 int(rand(n))+1;��n�ɂ͕\��������p�^�[���̐�������B
sub town_jouhou {
 $news_rand = int(rand(4))+1;
 if ($news_rand == 1){
  $news_bar = $news_bar1;
 }elsif ($news_rand == 2){
  $news_bar = $news_bar2;
 }elsif ($news_rand == 3){
  $news_bar = $news_bar3;
  }else{
   $news_bar = $news_bar4;
  }
 $keizai_hyouzi = int ($keizai / (int(($date_sec - $t_yobi2)/(60*60*24))+1));
 $hanei_hyouzi = int ($hanei / (int(($date_sec - $t_yobi2)/(60*60*24))+1));
 print <<"EOM";
<table width="100%" border="0" cellspacing="0" cellpadding="0" align=center class="yosumi" background="$img_dir/townnameback.gif">
<tr bgcolor="white"><td><img src="$img_dir/ar.gif" alt="�G���A��"></td><td><img src="$img_dir/dt.gif" alt="�G���A�f�[�^"></td></tr><tr><td><div align=center><span  class="tyuu">�u<B>$title</B>�v��</span><br><span  class="midasi">$town_name</span></div></td><td><span  onMouseOver='onMes5("���̊X�̓y�n�̉��i")' onMouseOut='onMes5("")'>�n�@���F$town_tika_hairetu[@_[0]]��</span><br><span  onMouseOver='onMes5("���̊X�̏Z���̂��X�̕��ςP������グ�z")' onMouseOut='onMes5("")'>�o�ϗ́F$keizai_hyouzi�~</span><br><span  onMouseOver='onMes5("���̊X�ɂ���f���̕��ςP���������ݐ�")' onMouseOut='onMes5("")'>�ɉh�x�F$hanei_hyouzi</td></tr><tr bgcolor="white"><td colspan="2"><img src="$img_dir/nt.gif" alt="�ŐV�g�s�b�N�X"></td></tr><tr><td colspan="2">$news_bar</span></td></tr></table><br>
EOM
}
 
#�R�}���h�{�^���̏o��
sub command_botan {			#ver.1.3	�����{�^���A�z��҉Ɛݒ�{�^���ǉ��A�q��ă{�^���ǉ��A���Ƃ����䂪�ƃ{�^���폜�A�{�^���̕��ѐ��ύX
    print "<img src=$img_dir/cm.gif alt=�R�}���h></td></tr><tr><td><tr><td background=$img_dir/cloud.gif>";
#�w�����t�@�C�����J��
	$monokiroku_file="./member/$k_id/mono.cgi";
	if (! -e $monokiroku_file){
		open (OUT,">$monokiroku_file") || &error("�����̍w�����t�@�C�����쐬�ł��܂���");
		eval{ flock (OUT, 2); };
		close(OUT);
	}
	open(OUT,"< $monokiroku_file") || &error("�����̍w�����t�@�C�����J���܂���");
	eval{ flock (OUT, 1); };
	@my_kounyuu_list =<OUT>;
	@mono_name_keys = ();
	@mono_kouka_keys = ();
	foreach (@my_kounyuu_list){
		&syouhin_sprit($_);
		if ($syo_taikyuu <= 0){next;}
		push (@mono_name_keys ,$syo_hinmoku);
		push (@mono_kouka_keys ,$syo_kouka);
	}
	$botanyou_mono_check = join("<>",@mono_name_keys);
	$botanyou_kouka_check = join("<>",@mono_kouka_keys);
	close(OUT);
	
	if ($renai_system_on == 1){$botan_narabi_suu = 7;}else{$botan_narabi_suu = 6;}

#koko2006/11/25
	if ($in{'mysec'}){
		($sec_dis,$min_dis,$hour_dis,$mday_dis,$mon_dis,$year_dis,) = localtime($in{'mysec'} + 60*$work_seigen_time);
	}else{
		($sec_dis,$min_dis,$hour_dis,$mday_dis,$mon_dis,$year_dis,) = localtime($house_name + 60*$work_seigen_time);
	}
	$year_dis += 1900;
	$mon_dis++;
	if ($min_dis < 10){$min_dis = '0'.$min_dis}
	if ($sec_dis < 10){$sec_dis = '0'.$sec_dis}

	$kaigyou_flag=1;
	$top_botan  .= <<"EOM";
<form method=POST name=ct action="$script"><td><input type=hidden name=std value='$year_dis $mon_dis $mday_dis $hour_dis $min_dis $sec_dis'><!--koko2006/04/01 --><input type=hidden name=mode value="login_view"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/reload.gif' width=32 height=32  onMouseOver='onMes5("��ʂ��X�V���܂��B�u�p���[�v�͋x����A���̃{�^�����������Ƃŏ��X�ɑ����܂��B")' onMouseOut='onMes5("")'></td></form>
EOM
#kokoend
	if ($job ne "�w��"){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}

	$top_botan  .= <<"EOM";
<!-- koko2006/04/01 -->
<script type="text/javascript">
<!--
//function my_sec(){ ������2007/04/25
//	myDate = Math.round((new Date()).getTime()/1000);
//	document.ctw.mysec.value = myDate;
//}
// #koko2006/12/25
function mese_on() {
	onMes5("�d���ɏo�����܂��B���݁A�o���l�F$job_keiken�@�Ζ����F$job_kaisuu��");
}
function mese_out() {
	Disp = document.foMes5.w_time.value;
	onMes5(Disp);
}
function mese_on2() {
	onMes5("���ݎd���A�o���l�F$job_keiken�@�Ζ����F$job_kaisuu��");
}

//-->
</script>
<form method=POST name=ctw action="basic.cgi"><td><INPUT TYPE=hidden NAME="mysec"><input type=hidden name=mode value="do_work"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=hidden name=cond value="$condition"><div id="comm"><input type=image src='$img_dir/go_work.gif' width=32 height=32 onMouseOver='mese_on()' onMouseOut='mese_out()'></div></td></form><!--ver.1.40-->
EOM
#kokoend
	}elsif(($brauza eq 'FireFox' || $brauza eq "") && $job ne "�w��"){ #koko2007/04/22
		print "<form method=POST name=ctw action=\"basic.cgi\"><td><INPUT TYPE=hidden NAME=\"mysec\"><input type=hidden name=mode value=\"do_work\"><input type=hidden name=name value=\"$in{'name'}\"><input type=hidden name=pass value=\"$in{'pass'}\"><input type=hidden name=k_id value=\"$k_id\"><input type=hidden name=town_no value=\"$in{'town_no'}\"><input type=hidden name=cond value=\"$condition\"><div id=\"comm\"><input type=image src='$img_dir/go_work.gif' width=32 height=32 onMouseOver='mese_on()' onMouseOut='mese_out()'></div></td></form><!--ver.1.40-->\n";
	}#kokoend

	
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="basic.cgi"><input type=hidden name=mode value="item"><td><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/item.gif' width=32 height=32  onMouseOver='onMes5("�A�C�e�����g�p���܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="$script"><td><input type=hidden name=mode value="aisatu"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/aisatu.gif' width=32 height=32  onMouseOver='onMes5("�����̏o������C���Ȃǂ����������܂��傤�B")' onMouseOut='onMes5("")'></td></form>
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="$script"><td><input type=hidden name=mode value="mail_sousin"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/mail.gif' width=32 height=32  onMouseOver='onMes5("�X�̏Z�l���ĂɃ��b�Z�[�W�𑗐M���邱�Ƃ��ł��܂��B")' onMouseOut='onMes5("")'></td></form>
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="game.cgi"><td><input type=hidden name=mode value="doukyo"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/doukyo.gif' width=32 height=32  onMouseOver='onMes5("�����̃L�����N�^�[���쐬����ĂĂ����܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="game.cgi"><td><input type=hidden name=mode value="battle"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/battle.gif' width=32 height=32  onMouseOver='onMes5("�X�g���[�g�t�@�C�g�ɏo�����܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM

	if ($unit{$k_id} ne ""){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="original_house.cgi"><td><input type=hidden name=mode value="my_house_settei">	<input type=hidden name=iesettei_id value="$k_id"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/my_housein.gif' width=32 height=32  onMouseOver='onMes5("�����̉ƂɊւ���e��ݒ���s���܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM
	}

	if ($unit{$house_type} ne ""){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="original_house.cgi"><td><input type=hidden name=mode value="my_house_settei"><input type=hidden name=iesettei_id value="$house_type"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/my_housein2.gif' width=32 height=32  onMouseOver='onMes5("�z��҂̉ƂɊւ���e��ݒ���s���܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM
	}
	
	if ($love >= $need_love && $renai_system_on == 1){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="kekkon.cgi"><td><input type=hidden name=mode value="renai"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/renai.gif' width=32 height=32  onMouseOver='onMes5("���l�ƃf�[�g��������A�v���|�[�Y������ł��܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM
	}
	
	if ($love >= $need_love && $renai_system_on == 1){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="kekkon.cgi"><td><input type=hidden name=mode value="kosodate"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/kosodate.gif' width=32 height=32  onMouseOver='onMes5("�q��Ă����܂��B")' onMouseOut='onMes5("")'></td></form><!--ver.1.40-->
EOM
	}
	
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan .="</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action="game.cgi"><td><input type=hidden name=mode value="data_hozon"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=image src='$img_dir/off.gif' width=32 height=32  onMouseOver='onMes5("�f�[�^�ۑ����܂��B�Ō�ɕۑ������H�����Ԃ�$deleteUser���𒴂���ƃ��[�U�[�폜����܂��B")' onMouseOut='onMes5("")'></td></form><!-- ver.1.40 -->
EOM

	print "<table boader=0 width=100%><tr>$top_botan</tr></table>";
#koko2007/10/26
	if($brauza eq 'Microsoft Internet Explorer'){
		if($in{'otoon'} && $in{'otodashi'} eq 'on'){
			$oto = 'on';
		}
		if($in{'otoon'} && $in{'otodashi'} ne 'on'){
			$oto = '';
		}
		if($oto eq 'on'){$checked_on = " checked";}

		&temp_routin;
		&log_kousin($my_log_file,$k_temp);

		print << "EOM";
<form method=POST action="$script" style="margin-top:0; margin-bottom:0;"><input type=hidden name=mode value="login_view"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=checkbox name=otodashi value="on"$checked_on>�����o��<input type=submit name=otoon value="OK"></form>
EOM
	}else{
		print "�u���E�U:$brauza"; #2006/11/30
	}
#end2007/10/26
}

#�l�p�����[�^�o��
sub loged_gamen {
#�p���[��MAX�l�v�Z
	$energy_max = int(($looks/12) + ($tairyoku/4) + ($kenkou/4) + ($speed/8) + ($power/8) + ($wanryoku/8) + ($kyakuryoku/8));
	$nou_energy_max = int(($kokugo/6) + ($suugaku/6) + ($rika/6) + ($syakai/6) + ($eigo/6)+ ($ongaku/6)+ ($bijutu/6));
	my ($date_sec) = time;
	
#�g�̃p���[�v�Z		#ver.1.3
	if ($in{'iiyudane'} eq "one"){
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$onsen_times);
	}elsif($in{'iiyudane'} eq "two"){
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$tokubetu_times);

#koko2006/03/31
	}elsif($in{'iiyudane'} eq "five"){ #matu
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$matu_times);
	}elsif($in{'iiyudane'} eq "fo"){ #take
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$take_times);
	}elsif($in{'iiyudane'} eq "three"){ #
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$ume_times);
#kokoend2006/03/31

	}else{
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku);#koko2007/05/30
	}
	$last_ene_time= $date_sec;

	if($energy > $energy_max){$energy = $energy_max;}
	if($energy < 0){$energy = 0;}
#���]�p���[�v�Z		#ver.1.3
	if ($in{'iiyudane'} eq "one"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$onsen_times);
	}elsif($in{'iiyudane'} eq "two"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$tokubetu_times);

#koko2006/03/31
	}elsif($in{'iiyudane'} eq "five"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$matu_times);
	}elsif($in{'iiyudane'} eq "fo"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$take_times);
	}elsif($in{'iiyudane'} eq "three"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$ume_times);
#kokoend2006/03/31

	}else{
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku);
	}
	$last_nouene_time= $date_sec;

	if($nou_energy > $nou_energy_max){$nou_energy = $nou_energy_max;}
	if($nou_energy < 0){$nou_energy = 0;}

#new���[���̃`�F�b�N
	$message_file="./member/$k_id/mail.cgi";
	open(MS,"< $message_file") || &error("�����̃��[�����O�t�@�C�����J���܂���");
	eval{ flock (MS, 1); };
	$lastCheckTime=<MS>;		#�ŏI���[�����Ԃ̎擾
	@lastMailTime=<MS>;		#���[���f�[�^�z��
	close(MS);
	foreach (@lastMailTime){
		&mail_sprit($_);
		if ($m_syubetu ne "���M"){$saigono_kita_mail = $m_byou;last;}
	}
#koko2007/09/28
	$i = 0;
	foreach (@lastMailTime){
		&mail_sprit($_);
		if ($m_syubetu eq "���M"){next;}
		if($lastCheckTime < $m_byou){++$i;}
	}
	@lastMailTime=split(/<>/,$lastMailTime);
	if($i){$i = "$i�ʂ�";}else{$i = "";}
	if($lastCheckTime < $saigono_kita_mail){$happend_ivent .= "<div style=color:#ff3300>����M����$i�V�������b�Z�[�W���͂��Ă��܂��I</div>";}

#koko2006/11/23
	$bbs1_log_file = "./member/$k_id/bbs1_log.cgi";

	if (-e "$bbs1_log_file"){
		open(IN,"< $bbs1_log_file") || &error("Open Error : $bbs1_log_file");
		eval{ flock (IN, 1); };
		# �擪�s���擾
		$total_counter = <IN>;
		close(IN);
		($total_counter,$all_total_counter,$kakikomijikan,$yomidashijikan)= split(/<>/, $total_counter);		#ver.1.40
		if ($yomidashijikan < $kakikomijikan){
			$happend_ivent .= "<div style=color:#ff3300>���f���ɐV�K����������܂��I</div>";
		}
	}
#kokoend2007/05/29
	if (-e "./member/$k_id/kaishiya_bbs.cgi"){
		open(KAISYA,"< ./member/$k_id/kaishiya_bbs.cgi") || &error("kaishiya_bbs.cgi�t�@�C�����J�����Ƃ��o���܂���ł����B");
		eval{ flock (KAISYA, 1); };
		$kanri_bbs = <KAISYA>;
		@kiji_bbs = <KAISYA>;
		close(KAISYA);

		($opn_no,$men_no,$kai_id,$kai_name_kanre,$kaitime,$kakikomijikan,$yomidashijikan) = split(/<>/,$kanri_bbs);
		if ($yomidashijikan < $kakikomijikan){
			$happend_ivent .= "<div style=color:#ff3300>����Ќf���ɐV�K����������܂��I</div>";
		}
	}
#kokoend

#�g�̃p���[�o�[�i���j�Z�o	
	if(! $energy_max){$energy_max =1;}
	$ener_parcent = int($energy / $energy_max * 100);
	$ener_parcent_disp = $ener_parcent * 2;#koko2005/03/22
	$nokori_parcent = 200-$ener_parcent_disp;#koko2005/03/22
	if ($ener_parcent >59){$energy_bar = "energy_ao.gif";}
	elsif ($ener_parcent >19){$energy_bar = "energy_ki.gif";}
	else{$energy_bar = "energy_aka.gif";}
	
#���]�p���[�o�[�i���j�Z�o	
	if(! $nou_energy_max){$nou_energy_max =1;}
	$nou_ener_parcent = int($nou_energy / $nou_energy_max * 100);
	$nou_ener_parcent_ds = $nou_ener_parcent * 2;#koko2005/03/22
	$nou_nokori_parcent = 200-$nou_ener_parcent_ds;#koko2005/03/22
	if ($nou_ener_parcent >59){$nou_energy_bar = "energy_ao.gif";}
	elsif ($nou_ener_parcent >19){$nou_energy_bar = "energy_ki.gif";}
	else{$nou_energy_bar = "energy_aka.gif";}

#�Ō�ɐH���������Ԃ���t�ɕϊ�
	&byou_hiduke($last_syokuzi);
	$last_syokuzi_henkan = $bh_full_date;
#�󕠓x���Z�o
	$tabetenaizikan = $date_sec - $last_syokuzi ;
	$manpuku_time = $syokuzi_kankaku*60;
	if ($tabetenaizikan < $manpuku_time){$kuuhukudo = "<font color=#ff3300>�����i�܂��H���ł��܂���j</font>";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*2 ){$kuuhukudo = "���x����";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*12 ){$kuuhukudo = "����";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*24 ){$kuuhukudo = "��";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*48 ){$kuuhukudo = "���Ȃ��";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*24*4 ){$kuuhukudo = "��������";}		#ver.1.3
	elsif ($tabetenaizikan < $manpuku_time + 60*60*24*($deleteUser - 3)){$kuuhukudo = "���ɂ����E�E";}		#ver.1.3
	else{$kuuhukudo = "��@���@���@�O";}		#ver.1.3
	
#BMI���`�F�b�N
	$taijuu = sprintf ("%.1f",$taijuu);
	&check_BMI($sintyou,$taijuu);

##�R���f�B�V�����v�Z
#�c�p���[������
$condition_sisuu = ($nou_ener_parcent + $ener_parcent)/2;
#���N�l������
$condition_sisuu += $kenkou / 100;
#�󕠓x������
if ($kuuhukudo eq "<font color=#ff3300>�����i�܂��H���ł��܂���j</font>"){$condition_sisuu *= 0.8;}elsif ($kuuhukudo eq "���x����"){$condition_sisuu *= 1;} elsif ($kuuhukudo eq "����"){$condition_sisuu *= 0.9;} elsif ($kuuhukudo eq "��"){$condition_sisuu *= 0.7;} elsif ($kuuhukudo eq "���Ȃ��"){$condition_sisuu *= 0.6;} elsif ($kuuhukudo eq "��������"){$condition_sisuu *= 0.5;}else{$condition_sisuu *= 0.3;} 
#�̌n�w��������
if ($taikei eq "�얞"){$condition_sisuu *= 0.8;}elsif ($taikei eq "��⑾��C��"){$condition_sisuu *= 0.95;} elsif ($taikei eq "�W��"){$condition_sisuu *= 1;} elsif ($taikei eq "�₹�C��"){$condition_sisuu *= 0.95;} else{$condition_sisuu *= 0.8;} 

if($condition_sisuu > 10000) {$condition = "���n�c���c�I�I"; $byouki_sisuu += 100}
elsif($condition_sisuu > 98) {$condition = "�ō�"; $byouki_sisuu += 2}
elsif($condition_sisuu > 75) {$condition = "�ǍD"; $byouki_sisuu += 1}
elsif($condition_sisuu > 50) {$condition = "����";}
elsif($condition_sisuu > 30) {$condition = "�s��"; $byouki_sisuu -= -1}
elsif($condition_sisuu > 10) {$condition = "����"; $byouki_sisuu -= 3}
else{$condition = "�ň�";}

if ($byouki_sisuu < -1000){$byoumei = "���S";}
elsif  ($byouki_sisuu < -600){$byoumei = "�A�����";}
elsif  ($byouki_sisuu < -300){$byoumei = "�����K��";}
elsif  ($byouki_sisuu < -150){$byoumei = "�K��";}
elsif  ($byouki_sisuu < -100){$byoumei = "�]���";}
elsif  ($byouki_sisuu < -70){$byoumei = "�S���a";}
elsif  ($byouki_sisuu < -40){$byoumei = "���j";}
elsif  ($byouki_sisuu < -20){$byoumei = "�x��";}
elsif  ($byouki_sisuu < -10){$byoumei = "����";}
elsif  ($byouki_sisuu < 0){$byoumei = "���ׂ���";}
else {$byoumei = "";}

if ($byoumei){$condition = "<font color=#ff6600>$byoumei</font>";}

#�W���u���x���Z�o
	$job_level = int($job_keiken / 100) ;

#�z�X�g�ۑ�
	$host = $get_host;
	
#���O�C����\��on off		#ver.1.30
	if ($in{'sanka_hyouzi_on'} eq "on"){$mise_type = "on";}		#ver.1.30
	if ($in{'sanka_hyouzi_on'} eq "off"){$mise_type = "off";}		#ver.1.30

#�ŏI�A�N�Z�X�ۑ�
	$last_access_byou = $access_byou;
	if ($in{'mode'} ne "syokudou" && $in{'mode'} ne "school" && $in{'mode'} ne "gym"){
		$access_byou = $date_sec;
	}

#���O�X�V
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);

#�l�p�����[�^�\��
	print <<"EOM";
<table width="100%" border="0" cellspacing="0" cellpadding="3" align=center>
<tr><td valign="top" width=65%>

<table  width="100%"  height="100% "border="0"  cellspacing="0" cellpadding="0" style=" border: $st_win_wak; border-style: solid; border-width: 1px;" bgcolor=$st_win_back><tr><td>
EOM

#���O�C�����[�h�Ȃ�R�}���h�{�^����\��
if ($in{'mode'} eq "login_view"){
	&command_botan;
#�������Ԃ�����ΐ����\��
#	&error("$koudou_seigen");
		if ($koudou_seigen > 0){
					if ($koudou_seigen > 999){$seigen_width = 5;}elsif($koudou_seigen > 99){$seigen_width = 4;}else{$seigen_width = 3;}
					$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $last_access_byou);
					$saikoroprint="<span style=\"color:#666666; font-size: 11px; \">�@�s���ł���܂ł���<input type=text name=cdown value=\"$koudou_seigen\" size=$seigen_width style='color:#ff3300; height: 10px; font-size: 11px; border: 0'>�b</span>";
		}
	
	print <<"EOM";
<table width="98%" border="0" cellspacing="0" cellpadding="5" align=center>
<tr><form  name=form1 method=POST action=\"$script\"><input type=hidden name=mode value="mail_sousin"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}">
<td  style="$message_window">
$happend_ivent$saikoroprint
</td></tr></form></table>
EOM
}
$next_levelup = 100 - ($job_keiken % 100);

#�Љ�L�[
	if ($syokai eq 'yes'){
		$no = $k_id;#koko2007/04/22
		if(!$syoukai_id){
			@arufabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');
			$moji1 = $arufabet[int(rand(26))];
			$moji2 = $arufabet[int(rand(26))];
			$suuji = sprintf("%02d",int(rand(100)));
			$moji3 = $arufabet[int(rand(26))];
			$moji4 = $arufabet[int(rand(26))];
			$syoukai_id = "$moji1$moji2$suuji$moji3$moji4";
#    #���O�X�V
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
		}
		$disp_syokai = "<span class=honbun2>�Љ�R�[�h�F</span>$syoukai_id=$no<br>";# koko2007/04/23
	}
#koko2007/09/27
	if ($dairekutoin eq 'yes2'||$dairekutoin eq 'yes3'){&kingakusyori;} 

#ver.1.3��������
	$money1 = $money;
	if ($money1 =~ /^[-+]?\d\d\d\d+/g) {
		  for ($i = pos($money1) - 3, $j = $money1 =~ /^[-+]/; $i > $j; $i -= 3) {
   			 substr($money1, $i, 0) = ',';
  		}
	}
	$k_sousisan1 = $k_sousisan;
		if ($k_sousisan1 =~ /^[-+]?\d\d\d\d+/g) {
  			for ($i = pos($k_sousisan1) - 3, $j = $k_sousisan1 =~ /^[-+]/; $i > $j; $i -= 3) {
    			substr($k_sousisan1, $i, 0) = ',';
  		}
	}
#ver.1.3�����܂�
#koko2007/04/28
	if (-e $job_keiken_f){
		open (IN,"< $job_keiken_f") || &error("�t�@�C�����J�����Ƃ��o���܂���ł����B");
		eval{ flock (IN, 1); };
		$job_keiken0 = <IN>;
		close(OUT);
	}
	chomp $job_keiken0;
	if ($job_keiken0){$disp_job = "<span class=honbun2>������</span>�F$job_keiken0";}
	unless($hatugen >= 1){$hatsugen_mes ="����";}
	else{$hatsugen_mes ="$hatugen";}
#kokoend
	print <<"EOM";
</td></tr><tr><td>
<img src="$img_dir/st.gif" alt="�X�e�[�^�X"></td></tr><tr><td background="$img_dir/main.gif">
<span class=honbun2>���@�O</span>�F$name<br>
$disp_syokai
<span class=honbun2  onMouseOver='onMes5(\"�����Y�������� + ���ʗa�� + �X�[�p�[��� - ���[���z\")' onMouseOut='onMes5(\"\")'>������</span>�F$money1�~<span class=small>�i�����Y�F$k_sousisan1�~�j</span><br>
<span class=honbun2  onMouseOver='onMes5(\"�o���l�F$job_keiken�i���̃��x���A�b�v�܂ł���$next_levelup�j�@�Ζ����F$job_kaisuu��\")' onMouseOut='onMes5(\"\")'>�E�@��</span>�F$job�i���x�� $job_level�j<br>

<!-- �p���[�o�[��\�\�� koko2005/03/22-->
<span class=honbun2  onMouseOver='onMes5(\"MAX�l�͐g�̃p�����[�^���グ�邱�Ƃő������܂��B\")' onMouseOut='onMes5(\"\")'>�g�̃p���[</span>�F$energy �iMAX�l�F$energy_max�j<br><img src="$img_dir/$energy_bar" width="$ener_parcent_disp" height="8"><img src="$img_dir/nokori_bar.gif" width="$nokori_parcent" height="8"><br>
<span class=honbun2 onMouseOver='onMes5(\"MAX�l�͓��]�p�����[�^���グ�邱�Ƃő������܂��B\")' onMouseOut='onMes5(\"\")'>���]�p���[</span>�F$nou_energy�iMAX�l�F$nou_energy_max�j<br><img src="$img_dir/$nou_energy_bar" width="$nou_ener_parcent_ds" height="8"><img src="$img_dir/nokori_bar.gif" width="$nou_nokori_parcent" height="8"> <br>
<span class=honbun2  onMouseOver='onMes5(\"�R���f�B�V�����́u�p���[�v�̉񕜓x�ɍł��e�����󂯂܂��i���ɂ��l�X�ȗv������j\")' onMouseOut='onMes5(\"\")'>�R���f�B�V����</span>�F$condition<br>
<span class=honbun2>�g�@�@��</span>�F$sintyou cm<br>
<span class=honbun2>�́@�@�d</span>�F$taijuu kg<br>
<span class=honbun2 onMouseOver='onMes5(\"�̊i�w��(BMI) = �̏d(kg) �� �g��(m) �� �g��(m)\")' onMouseOut='onMes5(\"\")'>�̊i�w��</span>�F$BMI�i$taikei�j<br>
<span class=honbun2  onMouseOver='onMes5(\"���Ȃ��̓o�^���Ă���̈��A���ł̔����񐔂ł��B��`���܂܂�܂��B\")' onMouseOut='onMes5(\"\")'>������</span>�F$hatsugen_mes <br>
<span class=honbun2  onMouseOver='onMes5(\"�O��̐H���F$last_syokuzi_henkan\")' onMouseOut='onMes5(\"\")'>�󕠓x</span>�F$kuuhukudo<br>
<!--ver.1.3��������-->
EOM
#koko2007/09/27
#�z��ҁA���l�̕\��
					open(COA,"< $couple_file") || &error("$couple_file�ɏ������߂܂���");
					eval{ flock (COA, 1); };
						@all_couple = <COA>;
					close(COA);
					foreach (@all_couple){
						($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
						if ($name eq "$cn_name1"){
							if ($cn_joutai eq "���l"){$my_koibito .= "$cn_name2�@";}
							elsif ($cn_joutai eq "�z���"){$my_haiguusya = "$cn_name2";}
						}
						if ($name eq "$cn_name2"){
							if ($cn_joutai eq "���l"){$my_koibito .= "$cn_name1�@";}
							elsif ($cn_joutai eq "�z���"){$my_haiguusya = "$cn_name1";}
						}
					}
					print <<"EOM";
					<span class=honbun2>�z���</span>�F$my_haiguusya<br>
					<span class=honbun2>���@�l</span>�F$my_koibito<br>
					<span class=honbun2>���L��</span>�F
EOM
#���L���̕\��
#koko2007/10/19
	if(!@my_kounyuu_list){
		$monokiroku_file="./member/$k_id/mono.cgi";
		open(OUT,"< $monokiroku_file") || &error("�����̍w�����t�@�C�����J���܂���");
		eval{ flock (OUT, 1); };
		@my_kounyuu_list =<OUT>;
		close(OUT);
	}
	foreach (@my_kounyuu_list){
		&syouhin_sprit ($_);
		if($syo_syubetu eq '�M�t�g'){
			push @syubetu1,$_;
		}elsif($syo_syubetu eq '�M�t�g���i'){
			push @syubetu2,$_;
			if($syo_taikyuu > 0){$morai_itemsuu++;} #koko2007/10/31
		}else{
			push @syubetu3,$_;
			if($syo_taikyuu > 0){$moti_itemsuu++;} #koko2007/10/31
		}
	}
#	$mochikazu = $#syubetu3 + 1; #koko2007/10/31
	print "<font color=#ff0099>�w�����i $moti_itemsuu</font><br>\n"; #koko2007/10/31
	foreach (@syubetu3){
		&syouhin_sprit ($_);

		if ($syo_taikyuu <=0){next;}
		if ($syo_hinmoku eq "���Ƃ����䂪��"){
			print <<"EOM";
<table boader=0 width=100%><tr><form method=POST action="original_house.cgi"><td><input type=hidden name=mode value="houmon"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=hidden name=ori_ie_id value="$k_id"><input type=image src='$img_dir/go_home2.gif' width=100 height=10  onMouseOver='onMes5("�����̉Ƃɍs�����Ƃ��ł��܂��B")' onMouseOut='onMes5("")'></td></form></tr></table><!--ver.1.40-->
EOM
			next;
		}

#koko2007/04/28  �����Ă鐔���o���B
		if ($kazu_disp eq 'yes'){
			if($syo_siyou_date + ($syo_kankaku*60) > time || (($syo_syubetu eq "�H���i" || $syo_syubetu eq "�t�@�[�X�g�t�[�h") && time < $last_syokuzi + ($syokuzi_kankaku*60))){
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}elsif($syo_syubetu eq "�M�t�g"){
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}else{
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}
		}else{
#koko2007/03/17
			if($syo_siyou_date + ($syo_kankaku*60) > time || (($syo_syubetu eq "�H���i" || $syo_syubetu eq "�t�@�[�X�g�t�[�h") && time < $last_syokuzi + ($syokuzi_kankaku*60))){
				print "��$syo_hinmoku ";
			}elsif($syo_syubetu eq "�M�t�g"){
				print "��$syo_hinmoku ";
			}else{
				print "��$syo_hinmoku ";
			}
		}
#		print <<"EOM";
#		��$syo_hinmoku�@
#EOM
#kokoend2007/03/17
	}
#	$mochikazu = $#syubetu2 + 1; #koko2007/10/31
	print "<br><font color=#ff0099>�M�t�g����������i $morai_itemsuu</font><br>\n"; #koko2007/10/31
	foreach (@syubetu2){
		&syouhin_sprit ($_);

		if ($syo_taikyuu <=0){next;}
		if ($syo_hinmoku eq "���Ƃ����䂪��"){
			print <<"EOM";
<table boader=0 width=100%><tr><form method=POST action="original_house.cgi"><td><input type=hidden name=mode value="houmon"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value="$in{'town_no'}"><input type=hidden name=ori_ie_id value="$k_id"><input type=image src='$img_dir/go_home2.gif' width=100 height=10  onMouseOver='onMes5("�����̉Ƃɍs�����Ƃ��ł��܂��B")' onMouseOut='onMes5("")'></td></form></tr></table><!--ver.1.40-->
EOM
			next;
		}
		if ($kazu_disp eq 'yes'){
			if($syo_siyou_date + ($syo_kankaku*60) > time || (($syo_syubetu eq "�H���i" || $syo_syubetu eq "�t�@�[�X�g�t�[�h") && time < $last_syokuzi + ($syokuzi_kankaku*60))){
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}elsif($syo_syubetu eq "�M�t�g"){
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}else{
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}
		}else{
			if($syo_siyou_date + ($syo_kankaku*60) > time || (($syo_syubetu eq "�H���i" || $syo_syubetu eq "�t�@�[�X�g�t�[�h") && time < $last_syokuzi + ($syokuzi_kankaku*60))){
				print "��$syo_hinmoku ";
			}elsif($syo_syubetu eq "�M�t�g"){
				print "��$syo_hinmoku ";
			}else{
				print "��$syo_hinmoku ";
			}
		}
	}
	$mochikazu = $#syubetu1 + 1;
	print "<br><font color=#ff0099>�M�t�g���鏤�i $mochikazu</font><br>\n";
	foreach (@syubetu1){
		&syouhin_sprit ($_);

		if ($syo_taikyuu <=0){next;}
		if ($kazu_disp eq 'yes'){
			if($syo_siyou_date + ($syo_kankaku*60) > time || (($syo_syubetu eq "�H���i" || $syo_syubetu eq "�t�@�[�X�g�t�[�h") && time < $last_syokuzi + ($syokuzi_kankaku*60))){
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}elsif($syo_syubetu eq "�M�t�g"){
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}else{
				print "��$syo_hinmoku($syo_taikyuu$syo_taikyuu_tani) ";
			}
		}else{
			if($syo_siyou_date + ($syo_kankaku*60) > time || (($syo_syubetu eq "�H���i" || $syo_syubetu eq "�t�@�[�X�g�t�[�h") && time < $last_syokuzi + ($syokuzi_kankaku*60))){
				print "��$syo_hinmoku ";
			}elsif($syo_syubetu eq "�M�t�g"){
				print "��$syo_hinmoku ";
			}else{
				print "��$syo_hinmoku ";
			}
		}
	}
#end2007/10/19
#ver.1.3�����܂�
	$nouryoku_goukeiti = $kokugo + $suugaku + $rika + $syakai + $eigo + $ongaku + $bijutu + $looks + $tairyoku + $kenkou + $speed + $power + $wanryoku + $kyakuryoku;
	foreach (6..22){
		$nouryoku_bar[$_] = int (($nouryoku_suuzi_hairetu[$_] / $nouryoku_goukeiti)*100*$nouryoku_goukeiti*0.002);
	}

#koko2007/09/27
		if($hozontown eq 'yes'){$disp_tag = "<input type=\"hidden\" name=\"town_no\" value=\"$ck{'town_no'}\">\n";}else{$disp_tag="";}
		if ($dairekutoin eq 'yes2' || $dairekutoin eq 'yes3'){
			$disp_tag = "<select name=\"town_no\">\n";
			$i=0;
			foreach (@town_hairetu){
				if($machikakushi eq 'yes'){#koko2007/10/21
					if($_ eq $kakushimachi_name && $kakushimachi_name || $_ eq $kakushimachi_name1 && $kakushimachi_name1 || $_ eq $kakushimachi_name2 && $kakushimachi_name2 || $_ eq $kakushimachi_name3 && $kakushimachi_name3 || $_ eq $kakushimachi_name4 && $kakushimachi_name4){
						$i++;
						next;
					}
				}
				$disp_tag .= "<option value=\"$i\">$_</option>\n";
				$i++
			}
			$disp_tag .= "</select><br>\n";

		}

sub kingakusyori{ #�����ɂ�����Ă��܂��E
	if(!$in{'fragu'}){
		$in{'mae_town'} = $in{'town_no'};
		$in{'fragu'} = 1;
	}elsif($in{'mae_town'} != $in{'town_no'}){
		$money =~ s/\,//g;
		$money -= 100000;
#���O�X�V
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);

		$in{'mae_town'} = $in{'town_no'};

	}
}

	print <<"EOM";
<br>$disp_job<br><!-- #koko2007/04/28 -->
<!-- ver.1.30 -->
EOM
if($dairekutoin eq 'yes2' || $dairekutoin eq 'yes3'){
	print <<"EOM";
	</td></tr><tr><td><img src="$img_dir/qj.gif" alt="�N�C�b�N�W�����v"></td></tr><tr><td background="$img_dir/qjback.gif"><BR>
<div align=center>
<form method=POST action="$script">
<input type=hidden name=mode value="login_view">
<input type=hidden name=name value="$in{'name'}">
<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=mae_town value="$in{'mae_town'}">
<input type=hidden name=fragu value="$in{'fragu'}">
$disp_tag<font color=#ff0000>�����̈ړ��ɂ�10��������܂��B</font><br>
<input type="submit" value='GO!'></form></div></td></tr>
EOM
	} #kokoend2007/09/27
	print <<"EOM";
</td></tr><tr><td><img src="$img_dir/at.gif" alt="������"></td></tr><tr><td bgcolor=#DDDDFF>
<div class=small>
���R���f�B�V�����ɂ���Ďd���œ�����o���l���ς���Ă��܂��B<BR>
���Q�[�����I������Ƃ��͕K���ۑ��{�^���������Ă��������B
</div></td></tr><tr><td><img src="$img_dir/bc.gif" alt="�f���E�`���b�g"></td></tr><tr><td bgcolor=#FFDDEE><font color=#ff0000>
<a href="http://matsupla.chatx.whocares.jp/" target=_blank>�V�^�V�i�O�_�j�X�N�鍑�����`���b�g</a><br><small>
������
<img alt="" width="24" height="12" src="http://matsupla.chatx.whocares.jp/mcond/users.png" />�l�A
ROM��
<img alt="" width="24" height="12" src="http://matsupla.chatx.whocares.jp/mcond/roms.png" />�l�ł��B</small><br><br>
<a href="http://snow.advenbbs.net/bbs/hira.htm" target=_blank>�s�n�v�m�����O���f����</a><br>
<small>�s�n�v�m�̑����I�ȃg���u���͂�����ցB</small><br>
<br>
<a href="http://bbs-r.com/m/g10works/" target=_blank>�G�k�f����</a><br>
<small>�����I�ȗp����G�k�Ȃǂ͂�����I</small><br>
<br>
<a href="http://w1.oekakies.com/p/g10works/p.cgi" target=_blank>G10���炭������[���</a><br>
<small>�G�����������Ȃ�����ǂ�����</small><br></font>
</td></tr><tr><td><img src="$img_dir/stf.gif" alt="�X�^�b�t"></td></tr><tr><td>
<span class=honbun2>����</span>�F�K�c�Õ��l<BR>
<span class=honbun2>�x�[�X�X�N���v�g</span>�F���������l<BR>
<span class=honbun2>����</span>�F�q�������[�E����<BR>
<span class=honbun2>����</span>�FG10�|Project<BR>
<span class=honbun2>�Ǘ��l</span>�F$admin_name<BR>
<span class=honbun2>���V�@�c��</span>�F$genrou_name[0]�E$genrou_name[1]<BR>
<span class=honbun2>���Ǘ��l</span>�F$fukukanrinin_name[0]�E$fukukanrinin_name[1]<BR>
<span class=honbun2>�Վ����Ǘ��l</span>�F$rinjiadmin
<br>
</td><tr>
</table>
</td><td align=right>
<!-- ver.1.30�������� -->
<table border="0"  cellspacing="0" cellpadding="0" style=" border: $st_win_wak; border-style: solid; border-width: 1px; font-size: 11px; line-height: 11px; color: #006699" bgcolor=$st_win_back width=100% height=100%>
<tr><td colspan=2><img src="$img_dir/pm.gif" alt="�p�����[�^"></td></tr>
<tr bgcolor=#DDFFAA><td colspan=2 align=center><BR><span class=tyuu>���@�]</span><BR></td></tr>
<tr bgcolor=#DDFFAA><td align=right>����F</td><td><table class=small><tr><td width=$nouryoku_bar[6] bgcolor=#cc0000><font color=#ffffff>$kokugo</font></td></tr></table></td></tr>
<tr bgcolor=#DDFFAA><td align=right>���w�F</td><td><table class=small><tr><td width=$nouryoku_bar[7] bgcolor=#0066cc><font color=#ffffff>$suugaku</font></td></tr></table></td></tr>
<tr bgcolor=#DDFFAA><td align=right>���ȁF</td><td><table class=small><tr><td width=$nouryoku_bar[8] bgcolor=#336633><font color=#ffffff>$rika</font></td></tr></table></td></tr>
<tr bgcolor=#DDFFAA><td align=right>�Љ�F</td><td><table class=small><tr><td width=$nouryoku_bar[9] bgcolor=#ff6600><font color=#ffffff>$syakai</font></td></tr></table></td></tr>
<tr bgcolor=#DDFFAA><td align=right>�p��F</td><td><table class=small><tr><td width=$nouryoku_bar[10] bgcolor=#ff0099><font color=#ffffff>$eigo</font></td></tr></table></td></tr>
<tr bgcolor=#DDFFAA><td align=right>���y�F</td><td><table class=small><tr><td width=$nouryoku_bar[11] bgcolor=#9900cc><font color=#ffffff>$ongaku</font></td></tr></table></td></tr>
<tr bgcolor=#DDFFAA><td align=right>���p�F</td><td><table class=small><tr><td width=$nouryoku_bar[12] bgcolor=#6666ff><font color=#ffffff>$bijutu</font></td></tr></table></td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td colspan=2 align=center bgcolor=#CCFFFF><BR><span class=tyuu>�g�@��</span><BR></td></tr>
<tr bgcolor=#CCFFFF><td  align=right nowrap>���b�N�X�F</td><td><table class=small><tr><td width=$nouryoku_bar[13] bgcolor=#ccff66>$looks</td></tr></table></td></tr>
<tr bgcolor=#CCFFFF><td align=right>�̗́F</td><td><table class=small><tr><td width=$nouryoku_bar[14] bgcolor=#ffcc00>$tairyoku</td></tr></table></td></tr>
<tr bgcolor=#CCFFFF><td align=right>���N�F</td><td><table class=small><tr><td width=$nouryoku_bar[15] bgcolor=#66ff66>$kenkou</td></tr></table></td></tr>
<tr bgcolor=#CCFFFF><td align=right nowrap>�X�s�[�h�F</td><td><table class=small><tr><td width=$nouryoku_bar[16] bgcolor=#99ffcc>$speed</td></tr></table></td></tr>
<tr bgcolor=#CCFFFF><td align=right>�p���[�F</td><td><table class=small><tr><td width=$nouryoku_bar[17] bgcolor=#ff9966>$power</td></tr></table></td></tr>
<tr bgcolor=#CCFFFF><td align=right>�r�́F</td><td><table class=small><tr><td width=$nouryoku_bar[18] bgcolor=#ff9999>$wanryoku</td></tr></table></td></tr>
<tr bgcolor=#CCFFFF><td align=right>�r�́F</td><td><table class=small><tr><td width=$nouryoku_bar[19] bgcolor=#ff99cc>$kyakuryoku</td></tr></table></td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td colspan=2 align=center bgcolor=#FFBBEE><BR><span class=tyuu>���̑�</span><BR></td></tr>
<tr bgcolor=#FFBBEE><td align=right>LOVE�F</td><td><table class=small><tr><td width=$nouryoku_bar[20] bgcolor=#ff9999>$love</td></tr></table></td></tr>
<tr bgcolor=#FFBBEE><td align=right>�ʔ����F</td><td><table class=small><tr><td width=$nouryoku_bar[21] bgcolor=#ffff66>$unique</td></tr></table></td></tr>
<tr bgcolor=#FFBBEE><td align=right>�G�b�`�F</td><td><table class=small><tr><td width=$nouryoku_bar[22] bgcolor=#cc99cc>$etti</td></tr></table></td></tr>
</table>
<!-- ver.1.30�����܂� -->
</td></tr></table>
EOM
}

###���O�o�b�N�A�b�v����
sub list_log_backup {
#	if ($in{'admin_pass'} ne $admin_pass){&error("�p�X���[�h���Ⴂ�܂�");}		#ver.1.22
#�t�H���_�[���̃t�@�C�������擾���ăo�b�N�A�b�v���O���쐬
					use DirHandle;
					$dir = new DirHandle ("./log_dir");
					while($file_name = $dir->read){ #1�ǂݍ����$folder_name�ɑ��
							if($file_name eq '.' || $file_name eq '..' || $file_name =~ /^backup_/ || $file_name eq '.DS_Store'){next;}
							my $backup_name = "backup_" ."$file_name";
							open (BK,"< ./log_dir/$file_name")  || &error("Open Error : ./log_dir/$file_name");
							eval{ flock (BK, 1); };
							my @back_data = <BK>;
							close (BK);
							if (@back_data != ""){
								open (BKO,">./log_dir/backup_dir/$backup_name") || &error("Write Error : ./log_dir/backup_dir/$backup_name");
								eval{ flock (BKO, 2); };
								print BKO @back_data;
								close (BKO);
							}
					}
					$dir->close;  #�f�B���N�g�������
}