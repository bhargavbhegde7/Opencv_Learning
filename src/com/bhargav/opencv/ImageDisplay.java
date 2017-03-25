/**
 * 
 */
package com.bhargav.opencv;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

/**
 * @author bhargava
 *
 */
public class ImageDisplay {
	
	public Mat openFile(String fileName) throws Exception{
		Mat newImage = Imgcodecs.imread(fileName);
		if(newImage.dataAddr()==0){
		throw new Exception ("Couldn't open file "+fileName);
		}
		return newImage;
		}
	
	static{
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
	}
	
	public static void main(String[] args) {
		String filePath = "C:/Users/bhargava/Desktop/pic1.png";
		Mat newImage = Imgcodecs.imread(filePath);
		System.out.println(newImage);
		if(newImage.dataAddr()==0){
			System.out.println("couldn't open file.");
		}else{
			ImageViewer imageViewer = new ImageViewer();
			imageViewer.show(newImage);
		}
	}
}
