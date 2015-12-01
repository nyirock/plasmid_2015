/*
 * fp.cpp
 *
 *  Created on: Jul 6, 2015
 *      Author: andriy
 */
#include<iostream>
#include<cstdlib>
#include<algorithm>// find(), search() count() functions
//#include <gmp.h>
//using std::count;

//using std::cout;
//using std::endl;

#include<map> //for key value relations

#include<vector>


#include<string>
using std::string;
#include <iterator>
#include <algorithm>
#include<cmath>//for pow() fucntion

#include"baseFive.h"

using namespace std;


int main(){
	char testBaseFive[50];

	//cout<<itoa(6, testBaseFive,5)<<endl;
	const char * filename="input_DNA.txt";
	char * buffer=readFile(filename);
	string genome=string(buffer);
	string text="ACTATAGCATGCATCGCCAGTGCATAGCATTGCCATGCTTAGCGGC";
	string text1="ACTATAGCATGCATCGCCAGTGCATAT";//28 characters
	string textNumber="231423412322412314121421432";//26 characters;
	string textNumbr2="1111111111111111111111111111";//27 characters almost maximum number, one digit more than the others
	string textNumbr3="444444444444444444444444444";//26 characters


	int k=18;
	vector <unsigned long> positions;
	vector <string> patternsBaseFive;

	for(int i=0;i<genome.length()-k+1;i++){
		string dnaText=genome.substr(i,k);
		string baseFive=dnaToBaseFive(dnaText);
		unsigned long baseTen=fromBaseFiveToTen(baseFive);
		//FrequentPatterns currentPattern(baseFive,baseTen);

		positions.push_back(baseTen);
		patternsBaseFive.push_back(baseFive);

	}

//	for(int i=0;i<positions.size();i++)
//		cout<<i<<" "<<baseFiveToDNA(patternsBaseFive[i])<<" "<<patternsBaseFive[i]<<" "<<positions[i]<<endl;
//	for(int i=0;i<positions.size();i++)
//		if(positions[i]==7)
//		cout<<"Position of \"AG\" is:"<<i<<endl;
//	unsigned long * a=&positions[0];
//	unsigned long *p;
//	//vector<long unsigned> myints={10,20,30,7,5,15,20};
//	p=find(a,a+46,positions[40]);
//	cout<<"element 7 is: "<<*p<<"At the position: "<<(p-a)<<endl;

	map <unsigned long, int> frequencyMap;
	for(int i=0;i<positions.size();i++){
		if(!frequencyMap.count(positions[i])>0){//value is unique
			int myCount=std::count(positions.begin(),positions.end(),positions[i]);
			frequencyMap[positions[i]]=myCount;
		}
	}

	int totalKeys=0;
	cout<<"Ten"<<" "<<"Five"<<" "<<"DNA"<<" "<<"Count"<<endl;
	for(map<unsigned long, int>::const_iterator it=frequencyMap.begin();it!=frequencyMap.end();++it){
		//totalKeys+=it->second;
		//if(it->second>100){
		cout<<it->first<<" "<<itoa(it->first,testBaseFive,5)<<" "<<baseFiveToDNA(itoa(it->first,testBaseFive,5))<<" "<<it->second<<endl;
		//}
	}

	//cout<<"Total patterns: "<<totalKeys<<"Map Size: "<<frequencyMap.size()<<endl;
	//cout<<"genome length: "<<genome.length()<<endl;

	return 0;
}
