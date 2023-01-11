#共発現しないensemblの組み合わせを各ファイルごとにまとめる
import csv
import glob
import os

#ファイルを保存するファルダを作成
dir_name = "not_exp_pairs"
os.makedirs(dir_name , exist_ok=True)

EA_files = glob.glob("/home/takahashiyuto/19rb046takahashiyuto/EA_TM_ens/*") #フォルダ内のすべてのファイルのパスを取得
for file in EA_files:
    file_name = file.split("/")[5]#ファイル名だけを取得
    
    inputfile = open("/home/takahashiyuto/19rb046takahashiyuto/EA_TM_ens/" + file_name)
    rows = csv.reader(inputfile,delimiter="\t")
    
    #読み込んだファイルのデータをリストにする
    rows_list = []
    for row in rows:
        rows_list.append(row)
    #print(rows_list)
    
    
    outputfile = open(dir_name + "/" + file_name,"a")
    outputfile.truncate(0)
    
    #2つの遺伝子の発現データのうち、どちらかが発現しなかったらnum_not_expという変数に1を足す。2つの遺伝子の発現データを全て調べ終わったらnum_not_expと発現データの個数を比べて同じ数なら2つのEnsemblをファイルに書き込む
    rows_num =len(rows_list)
    num_not_exp = 0
    for num1 in range(1,rows_num - 1):
        for num2 in range(num1 + 1,rows_num):
            #print(num)
            
            #2つの遺伝子の発現データを用意
            list_ens1 = [n for n in rows_list[num1]]
            list_ens2 = [m for m in rows_list[num2]]
            
            #list_ens1と2を比べる。1列目はEnsembl,2列目はgene nameなので発現情報は3列目から
            for ens1,ens2 in zip(list_ens1[2:],list_ens2[2:]):
                #print(ens1 + "  ",ens2)
                if ens1 == "" or ens2 == "": #発現しないときは何も書かれていないので""
                    num_not_exp += 1
                    #print(list_ens1[0])
                    #print(ens1,ens2)
            #print(num_not_exp,len(list_ens1[2:]))
            #print(not_exp_pair)
            
            #ファイルに書き込む
            if num_not_exp  == len(list_ens1[2:]):
                print(list_ens1[0],list_ens2[0])
                #not_exp_pair = [list_ens1[0],list_ens2[0]]
                outputfile.writelines(list_ens1[0] + "  " + list_ens2[0] +"\n")
            num_not_exp = 0
                


#print(rows_list)
        