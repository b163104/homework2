# homework2
- ガンマ変換の説明
ガンマの値をトラックバーで受け取り、ガンマ変換する。
ルックアップテーブルを使い、それぞれの輝度値について、トラックバーから受け取ったガンマ値を適応させる。

    look_up_table = np.ones((256, 1), dtype = 'uint8' ) *　0
    for i in range(256):
        look_up_table[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
        
ガンマの値がゼロになるのを防ぐために、トラックバーから受け取った値に0.0001をプラスする。
  
      gamma=v
    gamma+=0.0001
   

- ガウシアンフィルタの説明
分散をトラックバーで受け取り、画像にガウシアンフィルタを適用する
分散を受け取り、フィルターでたたみこむ
今回は、17*17のガウシアンフィルタを適応した

      blur = cv2.GaussianBlur(frame,(17,17),v)
   
- カラーチェンジの説明


##　動画へのリンク
https://www.youtube.com/watch?v=FAzn_79jFr4
//ガンマ変換

https://www.youtube.com/watch?v=jQApGRScn0c
//ガウシアンフィルタの実装

https://www.youtube.com/watch?v=Jt-CGPxWVUo
//カラーチェンジ

##　参考文献
https://www.blog.umentu.work/python-opencv3%E3%81%A7%E3%82%AC%E3%83%B3%E3%83%9E%E5%A4%89%E6%8F%9Bgamma-conversion-2/

http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_filtering/py_filtering.html

http://rasp.hateblo.jp/entry/2016/01/24/214027
