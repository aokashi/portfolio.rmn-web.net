var jx = 300;
var jy = 50;
var mx = 40;
var my = 120;
var randed;
var canvas;

window.onload=init;
function init(){
	var canvas = document.getElementById("movie");
	canvas = canvas.getContext("2d");//.getContext(x)�Fcanvas �ɕ`�悷�邽�߂� API �ɃA�N�Z�X�ł���I�u�W�F�N�g��Ԃ��B ���T�|�[�g��null
		
	canvas.scale(2,2);
	
  	canvas.fillText("�E�ցE",jx,jy);
  	canvas.fillText("�E�~�E",mx,my);
  	setInterval(function(){
		canvas.clearRect(0,0,960,320);
		canvas.beginPath();
		canvas.fillText("�E�ցE",jx,jy);
		jx+=randomMove();
		jy+=randomMove();
		
		canvas.fillText("�E�~�E",mx,my);
		mx+=randomMove();
		my+=randomMove();

  	},50);
}

function randomMove(){
	randed = Math.floor((Math.random()*2));
	if(randed == 0){return -3;}
	else{return 3;}
}