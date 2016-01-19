/**
 * 
 */
package com.bhargav.opencv;

/**
 * @author bhargava
 *
 */
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;
import javax.swing.WindowConstants;

import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;

public class ImageViewer {
	
	private JLabel imageView;
	public void show(Mat image){
		show(image, "");
	}
	
	/* ------------------------------------- */
	
	public Mat getBlurredImage(Mat source){
		Mat destination = new Mat(source.rows(),source.cols(),source.type());
        Imgproc.GaussianBlur(source, destination,new Size(45,45), 0);
		return destination;
	}
	
	public Mat getHSVImage(Mat source){
		Mat destination = new Mat(source.rows(),source.cols(),source.type());
		Imgproc.cvtColor(source, destination, Imgproc.COLOR_RGB2HSV);
		return destination;
	}
	
	public Mat getMaskInRange(Mat source){
		Mat destination = new Mat(source.rows(),source.cols(),source.type());
		Core.inRange(source, new Scalar(17, 168, 112), new Scalar(255, 255, 255), destination);
		return destination;
	}
	
	public Mat getEroded(Mat source){
		int erosion_size = 5;
		Mat element = Imgproc.getStructuringElement(Imgproc.MORPH_RECT, new  Size(2*erosion_size + 1, 2*erosion_size+1));
		Mat destination = new Mat(source.rows(),source.cols(),source.type());
        Imgproc.erode(source, destination, element);
        return destination;
	}
	
	public Mat getDilated(Mat source){
        int dilation_size = 5;
        Mat element1 = Imgproc.getStructuringElement(Imgproc.MORPH_RECT, new  Size(2*dilation_size + 1, 2*dilation_size+1));
        Mat destination = new Mat(source.rows(),source.cols(),source.type());
        Imgproc.dilate(source, destination, element1);
        return destination;
	}
	
	/* ------------------------------------- */
	
	public void show(Mat image,String windowName){
		setSystemLookAndFeel();
		JFrame frame = createJFrame(windowName);
		
		
		/* --------------- */
		Mat blurredImage = getBlurredImage(image);
		Mat hsv = getHSVImage(blurredImage);
		
		Mat mask = getMaskInRange(hsv);
			mask = getEroded(mask);
			mask = getDilated(mask);

		/* --------------- */
		
		Image loadedImage = toBufferedImage(mask);
		imageView.setIcon(new ImageIcon(loadedImage));
		frame.pack();
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);
	}
	
	private JFrame createJFrame(String windowName) {
		JFrame frame = new JFrame(windowName);
		imageView = new JLabel();
		final JScrollPane imageScrollPane = new JScrollPane(imageView);
		imageScrollPane.setPreferredSize(new Dimension(640, 480));
		frame.add(imageScrollPane, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		return frame;
	}
		
	private void setSystemLookAndFeel() {
		try {
		UIManager.setLookAndFeel
		(UIManager.getSystemLookAndFeelClassName());
		} catch (ClassNotFoundException e) {
		e.printStackTrace();
		} catch (InstantiationException e) {
		e.printStackTrace();
		} catch (IllegalAccessException e) {
		e.printStackTrace();
		} catch (UnsupportedLookAndFeelException e) {
		e.printStackTrace();
		}
	}
		
	public Image toBufferedImage(Mat matrix){
		int type = BufferedImage.TYPE_BYTE_GRAY;
		if ( matrix.channels() > 1 ) {
		type = BufferedImage.TYPE_3BYTE_BGR;
		}
		
		int bufferSize = matrix.channels()*matrix.cols()*matrix.rows();
		byte [] buffer = new byte[bufferSize];
		matrix.get(0,0,buffer); // get all the pixels
		BufferedImage image = new BufferedImage(matrix.cols(),matrix.
		rows(), type);
		final byte[] targetPixels = ((DataBufferByte) image.getRaster().
		getDataBuffer()).getData();
		System.arraycopy(buffer, 0, targetPixels, 0, buffer.length);
		return image;
	}		
}