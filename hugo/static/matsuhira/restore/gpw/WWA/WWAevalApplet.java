////////////////////////////////////////////////////////////////////////////////////////////////
// WWAevalApplet
// WWAeval��Applet�̋@�\���g�����߂ɍ쐬�����v���O�����ł��B
////////////////////////////////////////////////////////////////////////////////////////////////
import java.applet.Applet;
import java.awt.*;
import java.io.*;
import java.net.*;
import java.util.*;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class WWAevalApplet extends Applet implements Runnable {


//�摜�̂���t�H���_�̑��΃p�X
String imgDir = "./img/";

//���[�h����摜�̃t�@�C����
//�t�@�C�����̔ԍ��Ɠ����Y����ImgCrop���u������܂�
String[] imgNames = {
	"300.png",
	"301.png",
	"302.gif",
	"303.gif",
	"304.png",
	"310.gif",
	"311.png",
};

//�摜�t�H���_���́A�ǂݍ��މ摜�t�@�C�����̈ꗗ������e�L�X�g�t�@�C��
//�u""�v�ȊO��ݒ肵���ꍇ���imgNames�̐ݒ�����D�悳��܂�
//String imgListTxt = "";
String imgListTxt = "imglist.txt";






boolean imgLoaded = false;
String errMes = "";
HashMap loadedImgs = new HashMap();
private static WWAevalApplet instance;
private static volatile Integer countOfMe = new Integer(0);

public void paint(Graphics g) {
	g.drawString("WWA�ǉ��摜�ǂݍ��ݗp�̃A�v���b�g�ł�", 16, 10);
}

public void start() {
	//�O�̂��ߓ���
	synchronized(countOfMe) {
		countOfMe = new Integer(countOfMe.intValue() + 1);
		if(countOfMe.intValue() > 1)
			System.out.println("�������o at WWAevalApplet");
	}
	
	instance = this;
	Thread thread = new Thread(this);
	thread.start();
}

public void stop() {

	synchronized(countOfMe) {
		countOfMe = new Integer(Math.max(0, countOfMe.intValue() - 1));
	}
	
	instance = null;
	try {
		WWAextendSub.getInstance().stop();
	}
	catch(NullPointerException e) {}
}

void LoadImage() {
	URL imgBase = getNormalizedURL(getDocumentBase(), imgDir);
	MediaTracker tracker = new MediaTracker(this);
	java.util.List imgList = new ArrayList();

	if(imgListTxt != null && imgListTxt.length() != 0) {
		URL u = null;
		BufferedReader br = null;
		try {
			u = new URL(imgBase, imgListTxt);
			br = new BufferedReader(new InputStreamReader(u.openStream(), "JISAutoDetect"));
			while (br.ready()) {
				String text = br.readLine().replaceAll("//.*$|\\s", "");
				if(text.length() == 0 || !text.matches(".*\\d.*"))
					continue;
				imgList.add(text);
			}
		} catch (Exception e) {
			addError(imgListTxt + "�̓ǂݍ��݂Ɏ��s���܂����B");
			e.printStackTrace();
		} finally {
			if (br != null) try { br.close(); } catch (IOException e) {}
		}
	}
	else {
		imgList = Arrays.asList(imgNames);
	}
	
	for(int i = 0; i < imgList.size(); i++) {
		
		String imgName = (String)imgList.get(i);
		Image img = null;
		Integer imgNo = null;
		
		Matcher m = Pattern.compile("\\d+").matcher(imgName);
		if(m.find()) {
			imgNo = Integer.valueOf(m.group());
		}
		else {
			addError("�u" + imgName + "�v�ɓY���Ƃ��Ďg�p���鐔��������܂���B");
			continue;
		}
		if(loadedImgs.get(imgNo) != null) {
			addError("�u" + imgName + "�v�Ɠ����ԍ��̓Y�������łɎg�p����Ă��܂��B");
			continue;
		}
		
		URL imgURL = getNormalizedURL(imgBase, imgName);
		if(imgURL == null) {
			addError("�u" + imgName + "�v�͕s���ȃt�@�C�����ł��B");
			continue;
		}
		if(imgURL.toExternalForm().indexOf(imgBase.toExternalForm()) != 0) {
			addError("�u" + imgName + "�v�͕s���ȃt�H���_�ʒu�ɃA�N�Z�X���Ă��܂��B");
			continue;
		}
		img = getImage(imgURL);
		
		tracker.addImage(img, 0);
		
		try {
			tracker.waitForID(0);
		}
		catch (InterruptedException e) {}
		
		if((checkImage(img, this) & ERROR) != 0 ){
			img = null;
			addError("�u" + imgName + "�v�����݂��Ȃ������[�U�[���I�t���C���œǂݍ��߂܂���ł����B");
			continue;
		}
		
		if(img != null)
			loadedImgs.put(imgNo, img);
		else
			addError("�u" + imgName + "�v���ǂݍ��߂܂���ł����B");
	}
}

URL getNormalizedURL(URL url, String relative) {
	try {
		return new URI(url.toString().replaceAll(" ", "%20")).resolve(relative.replaceAll(" ", "%20"))
						.normalize().toURL();
	}
	catch(Exception e) {
		addError("URL�̉�͂Ɏ��s���܂����Brel�F" + relative);
		e.printStackTrace();
		return null;
	}
}

void addError(String err) {
	errMes = errMes.concat(err).concat("\n");
	System.out.println(err);
}

public void run() {
	LoadImage();
	imgLoaded = true;
}

public static WWAevalApplet getInstance() {
	//�Ȃ������炿����Ƒ҂�
	for (int i = 0; i < 10; i++) {
		if(instance != null) return instance;
		
		try {
			Thread.sleep(300);
		} catch (InterruptedException e){
		}
	}
	return null;
}

public static boolean isInterfered() {
	//�����Ȃ��ł�����
	return countOfMe.intValue() > 1;
}

public HashMap getImage() {
	return imgLoaded ? loadedImgs : null;
}

public String getErrMes() {
	return errMes.length() == 0 ? null : errMes;
}

public void soundPlay(String name) {
	//�����t�@�C�������[�h���Ă��邱�Ƃ��O��
	//�c�������Java���œǂݍ��܂�Ă��烊���[�h���Ȃ��񂾂�ˁH
	//JRE4�Ȃ烊���[�h���Ȃ��悤�����E�E�E
	play(getDocumentBase(), name + ".au");
}

}