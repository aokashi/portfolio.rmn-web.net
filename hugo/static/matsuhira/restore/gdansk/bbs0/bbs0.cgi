#!/usr/local/bin/perl

##### �J���L�^�Ȃ� ############
# 2007/05/17 
# Edit:�a�a�r(���������)
# 		Ver1.16
#
# bbs0.cgi	  700(�p�[�~�b�V����)
# kiroku.cgi	  600(�p�[�~�b�V����)
# host_kanri.cgi�@600(�p�[�~�b�V����)
##### �ݒ� ####################
# ���̂������̃t�@�C���̖��O
$this_cgi = 'bbs0.cgi';

# �^�C�g���̖��O
$this_name = '�a�a�r�[��';

#�^�C�g���̉摜
$this_img = "./img/bbs0.gif";

# �I�[�i�[�p�X�̐ݒ�(�ύX���Ă�������)
$ona_pas = '1234';

# ���Ǘ��Җ�
$kanre_name = '���������';

# �Ǘ��҂�������܂Ō��\���Ȃ�����1,���J�̎� 0,
$kanri = 1;

#�����b�̋���(����=1,�g��Ȃ�="")
$naisyo_kyka = 1;

#�p�����݂̂̓��e�֎~(�֎~=1,����="")
$eiginomi_dame = 1;

#URL�̃}�b�`����(1�`����URL��)
$mach = 2;

#�S�p�󔒂̐��̃Z�b�g�@�S�p�󔒂��w�蕶���ȏ㑱�����瓙���t�H���g�ɂȂ�B0�͎g��Ȃ�
$zenkaku_kuuhaku = 3;

#�I�[�g���s���� ���p������
$tab_chengi = 100;

# �w�i�F
$this_bgcolor ="#add8e6";

#�߂�A�h���X"./homu.htm";
$modoru = "<br><input type=\"button\" value=\"�I��\" onClick=\"window.close()\""; #�V�����E�C���h�[�ŊJ������
#$modoru = "<a href=\"./homu.htm\">�I��</a>";  #�����N�Ŗ߂�

#�S�̂̐ݒ�
$bak_set = "background=\"./img/tatu.gif\"  style=\"background-attachment: fixed;\"";
# �e�[�u���̐F
$taitol_bgcolor = "#ffa500";
$name_bgcolor = "#7cfc00";
$comento_bgcolor = "#ffffff";
$table_bac = "#ffffff";

# ���̋L�^�t�@�C��
$bbs_kiroku = "kiroku.cgi";

# ���X���t���Ə�ɏグ�� 1�ŃA�b�v
$res_up = 1;

# �\���X���b�h�i�����e�\�����邩�j
$suredosu = 30;

# �P�X���b�h�̓��e���E 0�̎��͐�������
$suredolimit =10;

# �P�y�[�W�ɕ\���̃X���b�h��
$pegi_limit = 6;

# New �̕\������ 24; ��24���� 0�͕\�����Ȃ�
$new_time = 24;

# �\�̕�
$waido = "90%";

# ���e�̑傫�� �o�C�g
$max_size = 8000;

# �O���A�N�Z�X�֎~�t�@�C���� koko2005/10/27 
$kinshiHostFaill = './host_kanri.cgi';

# GET �̕s���@1
$get_no = 1;

# �~�j�J�E���^�̐ݒu
#  �� 0=no 1=�e�L�X�g 2=�摜
$counter = 2;

# �~�j�J�E���^�̌���
$mini_fig = 5;

# �e�L�X�g�̂Ƃ��F�~�j�J�E���^�̐F
$cntCol = "#DD0000";

# �摜�̂Ƃ��F�摜�f�B���N�g�����w��
#  �� �Ō�͕K�� / �ŕ���
$gif_path = "./img/";
$mini_w = 27;		# �摜�̉��T�C�Y
$mini_h = 44;		# �摜�̏c�T�C�Y

# �J�E���^�t�@�C��
$cntfile = './count.dat';

# �o�^����N�b�L�[�̖��O
$COOKIE_NAME = 'bbs';
# �N�b�L�[�̗L������
$COOKIE_LIFE = 30;
##### �ݒ�I�� ################
&acsesu;	#�A�N�Z�X�֎~
&loadformdata;	#�t�H�[������
&load_cookie;	#�N�b�L�[��������
&yomikomi;	#�f�[�^�[�Ǎ�
if ($FORM{'kanri'} eq 'on'){&a_kanri;}  #�A�N�Z�X�֎~�̉���
if ($FORM{'acusesu'} ne ""){&acusesu;}  #�A�N�Z�X�֎~�o�^
if ($FORM{'edit'} ne ""){&edit;}	#�Ǘ��ҕҏW�@#koko2006/06/21
if ($FORM{'kanri_ck'} ne ""){&kanri;}	#�Ǘ�����
if ($FORM{'res'} ne ""){&res_modo;}	#���X                #####
if ($FORM{'del'} ne ""){&dele;}		#�폜�\��
if ($FORM{'ouna_del'} ne ""){&ohua_del;}#�I�[�i�[�̋L���폜koko2006/03/28
&kakicomi;	#��������
&set_cookie;	#�N�b�L�[�ɒl���Z�b�g
&print_http_header;	#�N�b�L�[�t���w�b�_�[���
&mein;		#�\��
exit;
### �A�N�Z�X�Ǘ� ##############
sub acsesu {
	$host = $ENV{'REMOTE_HOST'};
	if (!$host){$host = $ENV{'REMOTE_ADDR'};} #koko2007/05/16
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq "" || $host eq $addr) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr; #koko2007/05/18
	}
	if ($host eq "") { $host = $addr; }

	if ($kinshiHostFaill){
		open (REDDAT, "$kinshiHostFaill") or &err2("Open Error: $kinshiHostFaill");
		eval{ flock (REDDAT, 2); };
		@denyHost = <REDDAT>;
		close (REDDAT);
	}

	$denyHost = join(" ", @denyHost);

	local($flag)=0;
	foreach ( split(/\s+/, $denyHost) ) {
		s/(\W)/\\$1/g;
		s/\*/\.\*/g;
		if ($host =~ /$_/i || $addr =~ /$_/i) { $flag=1; last; }
	}
	if ($flag) { &err2("�A�N�Z�X��������Ă��܂���"); }

}
### �f�[�^�Ǎ� #################
sub yomikomi{
	open (COUNT, "<$bbs_kiroku") or &err2("�G���[�E�t�@�C�����J���܂���1");
	eval{ flock (COUNT, 2); };
	$cout_ima0 = <COUNT>;
	@kiroku = <COUNT>;
	close (COUNT);

	($cout_ima,$koment_bak) = split(/<>/, $cout_ima0);
	chomp $cout_ima0;
}
##### ���C�������@#############
sub mein{
	&header;	# �w�b�_�[���Ăяo��
	&form;		# �����ɓ��̓t�H�[��������
#	print "<hr width=\"$waido\" align=\"center\">\n";
	$i=0;
	
	$loop = 0;
	$end_loop =$#kiroku;
	$stato_point = 0;

	if ($FORM{'ato'} ne "" && $FORM{'pegi_a'} <= $end_loop -1){
		
		$loop = $FORM{'pegi_a'};
		++$loop;
		$stato_point = $loop;
	}else{
		$loop = $FORM{'pegi_m'};
		$stato_point = $FORM{'pegi_m'};
	}
	if ($FORM{'mae'} ne ""){
		$i = $FORM{'pegi_m'}-1;
		--$i;
		while ($i > 0){
#$loop_err++;if($loop_err > 200){err("loop_err 1");} #test
			(@kiroku2) = split(/<>/ ,$kiroku[$i]);
			if ($kiroku2[1] eq ""){
				++$loop;
			}
			--$i;
			if ($loop > $pegi_limit){last;}
		}
		if ($i < 0){$i = 0;}

		$stato_point = $i;
		$loop = $stato_point;
	}
	if ($loop eq ""){$loop = 0;}
	@kiroku2 = ();

	while ($loop <= $end_loop && $loop >= 0){
#$loop_err++;if($loop_err > 200){err("loop_err 2");} #test
		($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/ ,$kiroku[$loop]);
		(@kiroku2) = split(/<>/ ,$kiroku[$loop+1]);
		$disp_in = "";
#koko2007/05/13

		if ($naisyo_kyka == 1 && $naisyo ne '' && !$COOKIE{'pasbbs'}){ #$count2
			$naisyo = '';
		}elsif($naisyo){
			$disp_in = "�����b";

			if(!($naisyo_kyka == 1 && $naisyo eq $COOKIE{'name'} || $name eq $COOKIE{'name'} || $COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'})){
				$name = '�����b';
				$title = '�����b';
				$comento = '�����b';
			}
		}

		if ($kanri ==1 && $cheku ne 'cheku' && $COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'}){
			$disp_in .= " $host_m<br><input type=\"submit\" name=\"kanri_ck\" value=\"����\">";
		}elsif($kanri ==1 && $cheku ne 'cheku'){
			$name = '�`�F�b�N�҂�';
			$title = '�`�F�b�N�҂�';
			$comento = '�`�F�b�N�҂�';
		}
#kokoend
		if ($COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'}){

			$disp_in .= "<input type=\"submit\" name=\"edit\" value=\"�ҏW\"><input type=\"submit\" name=\"acusesu\" value=\"�A�N��\"><input type=\"submit\" name=\"ouna_del\" value=\"�L���폜\">";#koko2006/06/21
		}
		#kokoend2006/03/28
		print "<form action=\"$this_cgi\" method=\"POST\">\n";
		print "<input type=\"hidden\" name=\"nomba0\" value=\"$loop\">\n";
		print "<input type=\"hidden\" name=\"acses_p\" value=\"$host_m\">\n";
		if ($count2 eq ""){
			print "<table border=\"0\" bgcolor=\"$table_bac\" align=\"center\" width=\"$waido\" class=\"t_class\" cellspacing=\"0\">\n";
		}else {
			print "<tr><td colspan=\"2\"><hr align=\"center\"></td></tr>\n";
		}
		print "<tr><td bgcolor=\"$taitol_bgcolor\">$count $title</td><td align=\"right\" bgcolor=\"$taitol_bgcolor\">$disp_in<input type=\"submit\" name=\"res\" value=\"Res\"></td></tr>\n";

		print "<tr><td bgcolor=\"$name_bgcolor\">$name</td>";
#koko2006/03/29
		if ($new_time > 0 && $count3+$new_time*60*60 > time){
			print "<td align=\"right\" bgcolor=\"$name_bgcolor\"><font color=\"#ff0000\">New $jikan</font></td></tr>\n";
		}else{
			print "<td align=\"right\" bgcolor=\"$name_bgcolor\">$jikan</td></tr>\n";
		}
#kokoend2006/03/29 koko2007/05/06 koko2007/05/16
		$font_family = "";
		if ($zenkaku_kuuhaku != 0){
			$zenkaku = "�@" x $zenkaku_kuuhaku;
			if ($comento =~ m/$zenkaku/ ){
				$font_family = "font-family: monospace;";
			}
		}

		print "<tr><td colspan=\"2\" bgcolor=\"$comento_bgcolor\" style=\"word-break: break-all $font_family font-size: small;\">";
		if ($comento =~ m/\t/ ){
			$mijisu = 0;
			$moji_over = "";
			(@coment) = split(/<br>/,$comento);
			foreach (@coment){
				$mijisu = length $_;
				if ($tab_chengi < $mijisu){ #�������w��
					$moji_over = "yes";
					last;
				}
			}
			$disp_pm = "<font color=\"$comento_bgcolor\">Tab </font>";
			if ($moji_over eq "yes"){
				$comento =~ s/\t/$disp_pm/g;
				$com_x = $comento;
			}else{
				$comento =~ s/<br>/\n/g;
				$com_x = "<pre>$comento</pre>";
			}
		}else{
			$com_x = $comento;
		}
		$comento = $com_x;

		print "$comento";
		print "</td></tr>\n";
#kokoend2007/05/06
		print "</form>\n";
		if ($kiroku2[1] eq ""){
			++$loop1;
			print "</table>\n";
			print "<hr width=\"$waido\" align=\"center\">\n";
		}

		$restato_point = $loop;
		++$loop;
		if ($loop1 >= $pegi_limit){last;}
	}

	print <<EOF ;
<table border="0" align="center">
<form action="$this_cgi" method="POST">
<input type="hidden" name="pegi_m" value="$stato_point">
<input type="hidden" name="pegi_a" value="$restato_point">
<tr><td><input type="submit" value="�O��" name="mae"></td>
</form>

<div align="center">
<form action="$this_cgi" method="POST">
<input type="hidden" name="pegi_m" value="$stato_point">
<input type="hidden" name="pegi_a" value="$restato_point">
<td><input type="submit" value="����" name="ato"></td>
</form>

<form action="$this_cgi" method="POST">
<td>�@�@�폜 No:<input type="text" name="nob" size="6" maxlength="6">
 �폜�p�X:<input type="text" name="pasbbs" size="20" maxlength="10">
<input type="submit" value="�폜" name="del"></td></tr>
</form>
</table>
EOF

	&footer;	# �t�b�^�[���Ăяo��
}
### �Ǘ��ҕҏW #####koko2006/06/21
sub edit{
	if ($FORM{'nomba0'} ne "" && $COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'}){ 
		($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/ ,$kiroku[$FORM{'nomba0'}]);

		if ($FORM{'comento'} ne ""){
			$kiroku[$FORM{'nomba0'}] = "$count<>$count2<>$count3<>$name<>$pasbbs<>$FORM{'title'}<>$FORM{'comento'}<>$jikan<>$cheku<>$naisyo<>$host_m<>\n";
			open (COUNT, ">$bbs_kiroku") or &err2("�G���[�E�t�@�C�����J���܂���2");
			eval{ flock (COUNT, 2); };
			print COUNT "$cout_ima0\n";
			print COUNT @kiroku ;
			close (COUNT);

			$title = $FORM{'title'};
			$comento = $FORM{'comento'};
		}

#$comento
		$comento0 = $comento;
		$comento0 =~ s/<br>/\n/g;
		$comento0 =~ s/&lt;/</g;
		$comento0 =~ s/&gt;/>/g;
		$comento0 =~ s/&quot;/"/g;
		$comento0 =~ s/&amp;/&/g;

		&header;	# �w�b�_�[���Ăяo��

		print <<EOF ;
<table border="0" align="center" width="$waido" class="t_class" cellspacing="0">
<tr><td bgcolor="$taitol_bgcolor">$count $title</td><td align="right" bgcolor="$taitol_bgcolor"></td></tr>
<tr><td bgcolor="$name_bgcolor">$name</td><td align="right" bgcolor="$name_bgcolor">$jikan</td></tr>
<tr><td colspan=\"2\" bgcolor="$comento_bgcolor">$comento</td></tr>
</table>
<hr width="$waido" align="center">
<table border="2" align="center" width="$waido" class=\"t_class\">
<form action="$this_cgi" method="POST">
<input type="hidden" name="nomba0" value="$FORM{'nomba0'}">
<tr><td>���O�F</td><td><input type="text" name="name" size="40" value="$name" maxlength="20">
<tr><td>�薼�F</td><td><input type="text" name="title" size="60" value="$title" maxlength="30"></td></tr>
<tr><td>���e�F</td><td><textarea name="comento" cols="60" rows="6">$comento0</textarea></td></tr>
<tr><td></td>
<td><input type="submit" name="edit" value="�ҏW"> <input type="reset" value="���Z�b�g">
</td></tr>
</table>
</form>
<hr width="$waido" align="center">
<form action="$this_cgi" method="POST">
<div align="center"><input type="submit" value="�ҏW�I��"></div>
</form>
EOF

		&footer;	# �t�b�^�[���Ăяo��
	} else {
		return;
	}
	exit;
}
### �������� ###########
sub kakicomi{
	if ($FORM{'name'} eq "" || $FORM{'comento'} eq ""){return;}
	if ($FORM{'title'} eq ""){$FORM{'title'} = "(^_^;A";}

	($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/, $kiroku[$FORM{'nomba'}]);
#	if ($FORM{'nomba'} ne ""){
#		(@kiroku1) = split(/<>/, $kiroku[$FORM{'nomba'}+1]);
#	}

#koko2007/02/01
	if ($eiginomi_dame){
		if ($FORM{'comento'} !~ m/[\x80-\xff]/){
			&err2("I refuse contribution.");
		}
	}
#kokoend
	#-------------------------------------------------
	#  URL�`�F�b�N�@koko2007/04/10
	#-------------------------------------------------
	$i=0;
	while ($FORM{'comento'} =~ m/https?\:[\w\.\~\-\/\?\+\=\:\@\%\;\#\%]/g){ #�@&���ςɂȂ�
		$i++;
		if ($i > $mach){
			&err2("Over of URL.");
		}
	}
#kokoend

	if ($FORM{'comento'} eq $koment_bak){return;}
	++ $cout_ima ;
	$count = $cout_ima;
	if ($FORM{'nomba'} eq ""){
		$count2 = "";
	}else{
		++$count2;
		$FORM{'title'} ="Re$count2�F".$FORM{'title'};
		
	}
	&get_time;
	$cheku = "";
	$coun3 = time;	#koko2006/03/29 new�@�Ȃǂ̐V���p
	$kakikomi = "$count<>$count2<>$coun3<>$FORM{'name'}<>$FORM{'pasbbs'}<>$FORM{'title'}<>$FORM{'comento'}<>$jikan<>$cheku<>$FORM{'naisyobanashi'}<>$host<><br>\n";

	#koko2006/03/29
	if ($suredolimit != 0){
		if ($FORM{'nomba'} ne ""){
			$i= $FORM{'nomba'};
			while(1){
#$loop_err++;if($loop_err > 200){err("loop_err 1");} #test
				(@kiroku0) = split(/<>/, $kiroku[$i]);
				if ($kiroku0[1] eq ""){last;}
				--$i;
			}
			while(1){
#$loop_err++;if($loop_err > 200){err("loop_err 2");} #test
				(@kiroku0) = split(/<>/, $kiroku[$i]);
				if ($kiroku0[0] ne ""){
					push @up_sledo,$kiroku[$i];
		#		splice @kiroku,$i,1;
					$i++;
					(@kiroku0) = split(/<>/, $kiroku[$i]);
					if ($kiroku0[1] eq ""){last;}
				}
			}
$test ="$#up_sledo";
			if ($#up_sledo +1 >= $suredolimit){
				&err2("�G���[�E�V�����X���b�h������Ă��������B<br><a href=\"$this_cgi\">�X�^�[�g</a>");
			}
		}
	}
	if ($FORM{'res2'}){splice @kiroku,$FORM{'nomba'}+1,0,$kakikomi;}
	@up_sledo = ();

	if($FORM{'nomba'} ne ""){
		if ($res_up == 1){
			$i= $FORM{'nomba'};
			while(1){
$loop_err++;if($loop_err > 200){err("loop_err 2");} #test
				($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/, $kiroku[$i]);
				if ($count2 eq ""){last;}
				--$i;
			}
			while(1){
$loop_err++;if($loop_err > 200){err("loop_err 2");} #test
				($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/, $kiroku[$i]);
				push @up_sledo,$kiroku[$i];
				splice @kiroku,$i,1;
				($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/, $kiroku[$i]);
				if ($count2 eq ""){last;}
			}
			@kiroku =(@up_sledo,@kiroku);
		}
	}else{
		unshift (@kiroku ,$kakikomi);
	}

	$i = 0;
	$ii = 0;
	foreach (@kiroku){
		(@kiroku1) = split(/<>/);
		if ($kiroku1[1] eq ""){
			$ii++;
			if ($ii > $suredosu){last;}
		}
		++$i;
	}

	$#kiroku = --$i;

	open (COUNT, ">$bbs_kiroku") or &err2("�G���[�E�t�@�C�����J���܂���2");
	eval{ flock (COUNT, 2); };
	print COUNT "$cout_ima<>$FORM{'comento'}<>\n";
	print COUNT @kiroku ;
	close (COUNT);
}
### �I�[�i�[�폜 ######�@koko2006/03/28
sub ohua_del{
	if ($FORM{'nomba0'} ne "" && $COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'}){ 
		(@kiroku0) = split(/<>/ ,$kiroku[$FORM{'nomba0'}]);
		(@kiroku1) = split(/<>/ ,$kiroku[$FORM{'nomba0'}+1]);

		if ($kiroku0[1] eq ""){
			if ($kiroku1[1] eq ""){
				splice @kiroku,$FORM{'nomba0'},1;
			}else{
				($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/ ,$kiroku[$FORM{'nomba0'}]);
				$kiroku[$FORM{'nomba0'}] = "$count<>$count2<>$count3<>�폜<>�폜<>�폜<>�폜<>$jikan<>$cheku<>$naisyo<>$host_m<><br>\n";
			}
		}else{
			splice @kiroku,$FORM{'nomba0'},1;
		}
		open (COUNT, ">$bbs_kiroku") or &err2("�G���[�E�t�@�C�����J���܂���2");
		eval{ flock (COUNT, 2); };
		print COUNT "$cout_ima<>$FORM{'comento'}<>\n";
		print COUNT @kiroku ;
		close (COUNT);
	}
#	$FORM{'nomba0'} = "";
}
#kokoend 2006/03/28
### �Ǘ��`�F�b�N ######
sub kanri{
	$i = 0;
	if ($FORM{'nomba0'} ne "" && $COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'}){ 
		($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/ ,$kiroku[$FORM{'nomba0'}]);
		$cheku = 'cheku';
		$kiroku[$FORM{'nomba0'}] = "$count<>$count2<>$count3<>$name<>$pasbbs<>$title<>$comento<>$jikan<>$cheku<>$naisyo<>$host_m<><br>\n";
		open (COUNT, ">$bbs_kiroku") or &err2("�G���[�E�t�@�C�����J���܂���3");
		eval{ flock (COUNT, 2); };
		print COUNT "$cout_ima0\n";
		print COUNT @kiroku ;
		close (COUNT);
	}
}

### �ȈՍ폜 #####
sub dele{
	$i = 0;
	if ($FORM{'nob'} ne "" && $FORM{'pasbbs'} ne ""){ 
		foreach (@kiroku){
			($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/);
			if ($count eq $FORM{'nob'} && $ona_pas eq $FORM{'pasbbs'}){
				$del_kaki = $i;
				last;
			}
			if ($count eq $FORM{'nob'} && $pasbbs eq $FORM{'pasbbs'}){
				$del_kaki = $i;
				last;
			}
			++$i;
		}
		if ($del_kaki ne ""){
			($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/, $kiroku[$del_kaki]);
			$kiroku[$del_kaki] = "$count<>$count2<>$count3<>�폜<>�폜<>�폜<>�폜<>$jikan<>$cheku<>$naisyo<>$host_m<><br>\n";
			open (COUNT, ">$bbs_kiroku") or &err2("�G���[�E�t�@�C�����J���܂���3");
			eval{ flock (COUNT, 2); };
			print COUNT "$cout_ima0\n";
			print COUNT @kiroku ;
			close (COUNT);
		}
	}
}

### �ԐM���� #####
sub res_modo{
	&header;	# �w�b�_�[���Ăяo��
	($count,$count2,$count3,$name,$pasbbs,$title,$comento,$jikan,$cheku,$naisyo,$host_m) = split(/<>/, $kiroku[$FORM{'nomba0'}]);
	$name0 = $name;
	$count2++;
	if ($cheku ne 'cheku'){	#koko2007/05/14
		$name = '�`�F�b�N�҂�';
		$title = '�`�F�b�N�҂�';
		$comento = '�`�F�b�N�҂�';
	}
	if (!($naisyo eq "" || $naisyo eq $COOKIE{'name'}||$name eq $COOKIE{'name'}|| $COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'})){
		$name = '�����b';
		$title = '�����b';
		$comento = '�����b';
	}

	print "<table border=\"0\" align=\"center\" width=\"$waido\" class=\"t_class\">\n";
	print "<tr><td>$count $title</td><td align=\"right\"></td></tr>\n";
	print "<tr><td>$name</td><td align=\"right\">$jikan</td></tr>\n";
	print "<tr><td colspan=\"2\">$comento</td></tr>\n";
#	print "</form>\n"; #koko2007/05/14
	print "</table>\n";


	$nomba = $FORM{'nomba0'};
	$toukou = 'res2';
	&form;
	print "<a href=\"$this_cgi\">���ǂ�</a></div>\n";
	&footer;	# �t�b�^�[���Ăяo��
}

### �t�H�[���쐬 #######
sub form{
	if ($count2){
		if ($naisyo){
			if ($naisyo eq 'naisyo'){
				$naisyo = $name0;
			}
			$chec = " checked";
		}
	}else{
		$naisyo = 'naisyo';
	}
	if ($COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'}){
		$disp_kanre = "<input type=\"checkbox\" name=\"kanri\" value =\"on\">�Ǘ����[�h";
	}
 #koko2007/05/14
	print <<EOF ;
<table border="2" align="center" width="$waido" class=\"t_class\">
<form action="$this_cgi" method="POST">
<input type="hidden" name="nomba" value="$nomba">
<tr><td>���O�F</td><td><input type="text" name="name" size="40" value="$COOKIE{'name'}" maxlength="20">
�����p�p�X�F<input type="password" name="pasbbs" size="20" value="$COOKIE{'pasbbs'}" maxlength="10">
<input type="checkbox" name="naisyobanashi" value="$naisyo"$chec>�����b(�p�X�v��)
</td></tr>
<tr><td>�薼�F</td><td><input type="text" name="title" size="60" maxlength="30">
$disp_kanre
</td></tr>
<tr><td>���e�F</td><td><textarea name="comento" cols="60" rows="6"></textarea></td></tr>
<tr><td></td>
<td><input type="submit" name="$toukou" value="���M����"> <input type="reset" value="���Z�b�g">
�@�@�N�b�L�[�N���A<input type="checkbox" name="coodel" value="clia">
</td></tr>
</table>
</form>
<hr width="$waido" align="center">
EOF
}

### �t�H�[����M ##########
sub loadformdata {
	my ($query,$pair);
	if($ENV{'REQUEST_METHOD'} eq 'POST') {
		read(STDIN, $query, $ENV{'CONTENT_LENGTH'});
	} else {
		$query = $ENV{'QUERY_STRING'};
		if ($get_no ==1 && $query ne ""){&err2("�G���[�EGET �֎~");}
	}
	my ($saizu)=length $query;
	if ($saizu > $max_size){&err2("�G���[�E�T�C�Y�I�[�o�[");}
	
	foreach $pair (split(/&/, $query)) {
		my ($key, $value) = split(/=/, $pair);
	
	# �����̃f�R�[�h
		$value =~ tr/+/ /;
		$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/chr(hex($1))/eg;
	
#		$value = jcode::euc($value);	# euc? sjis? jcode.pl���K�v
		$value =~ s/&/&amp;/g;
		$value =~ s/</&lt;/g;
		$value =~ s/>/&gt;/g;
		$value =~ s/"/&quot;/g;
		$value =~ s/\x0D\x0A/<br>/g;
	#	$value =~ tr/\t/ /; #2007/05/06
	
		$FORM{$key} = $value;
	}
}

### ���݂̎��ԏo�� ###############
sub get_time{
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time) ;	#�ꊇ������
	$year += 1900;	# $year = $year + 1900 �Ɠ���
	++$mon ;
	@youbi=('��','��','��','��','��','��','�y');

	$mond = sprintf("%02d",$mon);
	$mdayd = sprintf("%02d",$mday);
	$hourd = sprintf("%02d",$hour);
	$mind = sprintf("%02d",$min);
	$secd = sprintf("%02d",$sec);

	$jikan = "$year�N$mond��$mdayd��$youbi[$wday]�j��$hourd��$mind��$secd�b";

#	$countup = 1;

}
### �N�b�L�[�ɒl���Z�b�g ####
sub set_cookie{
	if ($FORM{'name'} && $FORM{'pasbbs'}){	#�����̎�����B
		if (!$FORM{'coodel'}){
			$COOKIE{'name'} = $FORM{'name'};
			$COOKIE{'pasbbs'}  = $FORM{'pasbbs'};
		}
	}
}
### �N�b�L�[�ǂݏo�� ######
sub load_cookie{
	my	($pair, $cpair);
	
	foreach $pair (split(/;\s*/, $ENV{'HTTP_COOKIE'})) {
		my	($name, $value) = split(/=/, $pair);
		
		# �P��̃N�b�L�[�l����%COOKIE�Ƀf�R�[�h
		if($name eq $COOKIE_NAME) {
			foreach $cpair (split(/&/, $value)) {
				my	($cname, $cvalue) = split(/#/, $cpair);
				
				$cvalue =~ s/%([0-9a-fA-F][0-9a-fA-F])/chr(hex($1))/eg;
				$COOKIE{$cname} = $cvalue;
			}
			last;
		}
	}
}

### �N�b�L�[���s ####
sub print_http_header{
	my	(@cpairs, $cname, $cvalue, $value);
	if ($FORM{'coodel'}){$COOKIE_LIFE = -1;}
	# %COOKIE��P��̃N�b�L�[�l�ɃG���R�[�h
	foreach $cname (keys %COOKIE) {
		$cvalue = $COOKIE{$cname};
		$cvalue =~ s/(\W)/sprintf("%%%02X", ord $1)/eg;
		push @cpairs, "$cname#$cvalue";
	}
	$value = join('&', @cpairs);
	
	# �O���j�b�W�W�����̕�����
	my	@mon_str = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
	my	@wdy_str = qw(Sun Mon Tue Wed Thu Fri Sat);
	my	$life = $COOKIE_LIFE * 24 * 60 * 60;
	my	($sec, $min, $hour, $mday, $mon, $year, $wday) = gmtime(time + $life);
	my	$date = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$wdy_str[$wday], $mday, $mon_str[$mon], $year + 1900, $hour, $min, $sec);
	
#	print "Content-type: text/html; charset=Shift_JIS\n";
#	print "Set-Cookie: $COOKIE_NAME=$value; expires=$date\n\n";
	print "Set-Cookie: $COOKIE_NAME=$value; expires=$date\n";
}

### �w�b�_�[ #######
sub header{
	print "Content-type:text/html; charset=Shift_JIS\n\n";
	print <<EOF ;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=Shift_JIS">
<meta http-equiv="Content-Style-Type" content="text/css">
<title>$this_name</title>
<style type="text/css">
<!--
h1{
  color: #ff6600 ;
}
.t_class{
  border: dashed 4px #339933 ;
}
td {
	word-break: break-all; /* koko2007/05/06 */
	}
-->
</style>
</head>
<BODY BGCOLOR="$this_bgcolor" $bak_set>
EOF

	print "<table border=\"0\" width=\"100%\"><tr><td width=\"250\">";
	&counter;
	print "</td><td align=\"center\">";
	print "<div align=\"center\"><img src=\"$this_img\" alt=\"$this_name\"</div>\n";
	print "</td><td width=\"250\"><br></td></tr></table>\n";
	print "<hr width=\"$waido\" align=\"center\">\n";

}

### �t�b�^�[ #########
sub footer{
#------------- �����X�^�[�g ---------------------
# print "test=$kiroku[$FORM{'nomba0'}]<br>";
#-------�@�t�H�[���v�f���@---------�@���͊m�F�p�@��ŏ�������
# print "<table border='1'>";
# print "<tr><th>�t�H�[���v�f��</th><th>�f�[�^</th></tr>";
#
# foreach $key (keys %FORM) {
#	print "<tr><th>$key</th><td>$FORM{$key}</td></tr>\n";
# }
# print "</table><br>";
#-------�@�N�b�L�[�v�f���@---------
# print "<table border='1'>";
# print "<tr><th>�N�b�L�[�v�f��</th><th>�f�[�^</th></tr>";
#
# foreach $key (keys %COOKIE) {
#	print "<tr><th>$key</th><td>$COOKIE{$key}</td></tr>\n";
# }
# print "</table><br>";
#----------------------------------
# print @kiroku;
#------------ �����܂Ō����p ----------------------
	print <<EOF ;
<div align="center">$modoru<div>
<div align="right">Edit:�a�a�r(���������)<br>
Ver1.16</div>
<!-- <hr width="$waido" align="center"> -->
</BODY>
</html>
EOF

	exit;
}
### �G���[�̎� #######
sub err2 {
#	print "Content-type:text/html; charset=Shift_JIS\n\n";
	print <<EOF ;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=Shift_JIS">
<meta http-equiv="Content-Style-Type" content="text/css">
<title>$this_name</title>
</head>
<BODY BGCOLOR="$this_bgcolor" $bak_set>
EOF

	print "<h2 align=\"center\">";
	print "$_[0]\n";
	print "</h2>\n";
	print <<EOF ;
<div align="right">Edit:�a�a�r(���������)<br>
Ver1.16</div>
</BODY>
</html>
EOF

	exit;
}

### �֎~�z�X�g�ݒ�
sub acusesu {
	open (REDDAT, "$kinshiHostFaill") or &err2("Open Error: $kinshiHostFaill");
	eval{ flock (REDDAT, 2); };
	@denyHost = <REDDAT>;
	close (REDDAT);

	unshift @denyHost," $FORM{'acses_p'}";

	open (REDDAT, "> $kinshiHostFaill") or &err2("Open Error: $kinshiHostFaill");
	eval{ flock (REDDAT, 2); };
	print REDDAT "@denyHost";
	close (REDDAT);
}

### �A�N�Z�X�֎~���X�g����̉���
sub a_kanri {
	if (!($COOKIE{'name'} eq $kanre_name && $ona_pas eq $COOKIE{'pasbbs'})){return;}

	open (REDDAT, "$kinshiHostFaill") or &err2("Open Error: $kinshiHostFaill");
	eval{ flock (REDDAT, 2); };
	@denyHost = <REDDAT>;
	close (REDDAT);

	if ($FORM{'botan_no'} ne ""){
		splice @denyHost,$FORM{botan_no}, 1;
		open (DAT, "> $kinshiHostFaill") or &err2("�G���[�E�t�@�C�����J���܂���$kinshiHostFaill");
		eval{ flock (DAT, 2); };
		print DAT @denyHost ;
		close (DAT);
	}

	&header;
	print "<div align=\"center\">\n";
	print "�������̃z�X�g������Ǝg���Ȃ��Ȃ�܂��B$kinshiHostFaill�@���X�g���J���ď����Ă��������B��<br>\n";
	print "<FORM ACTION=\"$this_cgi\" METHOD=POST>\n";
	print "<input type=\"hidden\" name=\"kanri\" value=\"on\">\n";
	print "<table border='1'>";
	print "<tr><th>�I��</th><th>�z�X�g��</th></tr>\n";
	$loop_index = 0;
	foreach (@denyHost) {
		print "<tr><td><input type=radio name=botan_no value=$loop_index>$loop_index</td><td>$_</td></tr>\n";
		$loop_index++;
	}
	print "</table><br>";
	print "<INPUT TYPE=SUBMIT VALUE=\"�폜\">\n";
	print "</form>\n";
	print "<a href=\"$this_cgi\">���ǂ�</a></div>\n";

	&footer;

	exit;
}
#-------------------------------------------------
#  �J�E���^����
#-------------------------------------------------
sub counter {
	local($count,$cntup,@count);
  $loop_err++;if($loop_err > 200){die;} #test

	# �{�����̂݃J�E���g�A�b�v
#	if ($countup eq '1') { $cntup=1; } else { $cntup=0; }
	$cntup=1;

	if(!-e "$cntfile"){&err2("Open Error: $cntfile");}
	# �J�E���g�t�@�C����ǂ݂���
	open(IN,"$cntfile") or &err2("Open Error: $cntfile");
	eval {flock(IN, 2);};
	$count = <IN>;
	close(IN);

	# IP�`�F�b�N�ƃ��O�j���`�F�b�N


#koko2005/10/29
	local($local_time);
	local($cnt, $ip,$kiroku_day,$keika_day,$today,$yestaday) = split(/:/, $count);
#	if ($host eq $ip || $cnt eq "") { $cntup=0; }

	# �J�E���g�A�b�v
	if ($cntup) {

		$local_time = time + (9*60*60);#GMT+9:00�␳
		if (!$kiroku_day){
			$kiroku_day = $local_time - ($local_time % (24*60*60));
		}
		if ($local_time - $kiroku_day > 24*60*60){
			$keika_day += int(($local_time - $kiroku_day)/(24*60*60));
			if ($local_time - $kiroku_day > 2*24*60*60){
				$yestaday = 0;
			}else{$yestaday = $today;}
			$kiroku_day = $local_time - ($local_time % (24*60*60));
			$today = 0;
		}
		$today++;
		if (!$keika_day){$keika_day = 0; }
		if (!$yestaday){$yestaday = 0; } 

		$cnt++;
		open(OUT,"> $cntfile") || &err2("Write Error: $cntfile");
		eval {flock(OUT, 2);};
		print OUT "$cnt\:$host:$kiroku_day:$keika_day:$today:$yestaday";
		close(OUT);
		if (-z $cntfile){
			open(OUT,"> $cntfile") || &err2("Write Error: $cntfile");
			eval {flock(OUT, 2);};
			print OUT "$cnt\:$host:$kiroku_day:$keika_day:$today:$yestaday";
			close(OUT);
		}

	}
	# ��������
	while(length($cnt) < $mini_fig) { 
		$cnt = '0' . $cnt;
$loop_err++;if($loop_err > 200){err("loop_err cunt");} #test
	}
	@count = split(//, $cnt);
	print "<TABLE border=\"0\"><TBODY>\n";
	print "<TR><TD rowspan=\"3\">\n";

	# GIF�J�E���^�\��
	if ($counter == 2) {
		foreach (0 .. $#count) {
			print "<img src=\"$gif_path$count[$_]\.gif\" alt=\"$count[$_]\" width=\"$mini_w\" height=\"$mini_h\">";
		}
	# �e�L�X�g�J�E���^�\��
	} else {
		print "<font color=\"$cntCol\" face=\"Verdana,Helvetica,Arial\">$cnt</font><br>\n";
	}
	print "</TD><td><font size=\"2\">�o��</font></td><td><font size=\"2\">$keika_day</font></td></TR>\n";
	print "<TR><td><font size=\"2\">����</font></td><td><font size=\"2\">$today</font></td></TR>\n";
	print "<TR><td><font size=\"2\">���</font></td><td><font size=\"2\">$yestaday</font></td></TR>\n";
	print "</TBODY></TABLE><br>\n";
#kokoend
}

### �I���B #########
__END__
                                                                                                                                                                                                                                                                                                                                             