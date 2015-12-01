/*
 * frequentPatterns.cpp
 *
 *  Created on: Jul 6, 2015
 *      Author: andriy
 */
#include <cstdio>
#include <cstdlib>
#include<iostream>
#include <vector>
#include <string>
#include<algorithm> //reverse() string function
using std::vector;
using std::string;
using std::cout;
using std::endl;
#include<cmath>//for pow() fucntion
using namespace std;
#include "baseFive.h"

string dnaToBaseFive(string textDNA){
	//len=textDNA.length();
	string textBaseFive=textDNA;
	for (int i=0;i<textDNA.length();i++){
		switch(textDNA[i]){
		case 'A':
		//case "a":
			textBaseFive[i]='1';
			break;
		case 'T':
		//case "t":
			textBaseFive[i]='3';
			break;
		case 'G':
		//case "g":
			textBaseFive[i]='2';
			break;
		case 'C':
		//case "c":
			textBaseFive[i]='4';
			break;
		default:
			textBaseFive[i]='0';
		}
	}
	return textBaseFive;
}

string baseFiveToDNA(string textBaseFive){
	//len=textDNA.length();
	string textDNA=textBaseFive;
	for (int i=0;i<textBaseFive.length();i++){
		switch(textBaseFive[i]){
		case '1':
		//case "a":
			textDNA[i]='A';
			break;
		case '3':
		//case "t":
			textDNA[i]='T';
			break;
		case '2':
		//case "g":
			textDNA[i]='G';
			break;
		case '4':
		//case "c":
			textDNA[i]='C';
			break;
		default:
			textDNA[i]='N';
		}
	}
	return textDNA;
}

unsigned long fromBaseFiveToTen(string baseFive){
	unsigned long result=0;
	std::reverse(baseFive.begin(),baseFive.end());
	//cout<<baseFive;
	string digit;
	for(int i=0;i<baseFive.length();i++){
		digit=baseFive[i];
		result=result+std::stoi(digit)*pow(5,i);
	}
	return result;
}

char * readFile(const char * filename){
	char * buffer=0;
	long length;
	FILE * f=fopen(filename, "rb");

	if (f){
		fseek(f,0,SEEK_END);
		length=ftell(f);
		fseek(f,0,SEEK_SET);
		buffer=(char *)malloc(length);
		//malloc(length);
		if(buffer){
			fread(buffer,1,length-1,f);
		}
		fclose(f);
	}


	return buffer;
}

void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}

//// Implementation of itoa()
////http://www.geeksforgeeks.org/implement-itoa/
char* itoa(unsigned long num, char* str, int base)
{
    int i = 0;
    bool isNegative = false;

    /* Handle 0 explicitely, otherwise empty string is printed for 0 */
    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }

    // In standard itoa(), negative numbers are handled only with
    // base 10. Otherwise numbers are considered unsigned.
    if (num < 0 && base == 10)
    {
        isNegative = true;
        num = -num;
    }

    // Process individual digits
    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }

    // If number is negative, append '-'
    if (isNegative)
        str[i++] = '-';

    str[i] = '\0'; // Append string terminator

    // Reverse the string
    reverse(str, i);

    return str;
}
