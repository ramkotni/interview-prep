package com.test.interviews;

import java.util.ArrayList;
import java.util.List;

public class VowelsAndConsonants {

	public static void main(String[] args) {

		String input = "This is a really simple sentence A1 B2";

		List count = CountofVowelsAndConsonants(input);
		System.out.println(" count ::" + count);

	}

	public static List CountofVowelsAndConsonants(String str) {

		int vowels = 0;
		int consonants = 0;
		List vcList = new ArrayList();

		if (str == null) {
			throw new IllegalArgumentException("String cant be null");
		}

		str = str.toLowerCase();

		for (int i = 0; i < str.length(); i++) {

			char ch = str.charAt(i);

			if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
				vowels++;
			} else if (ch >= 'a' && ch <= 'z') {
				consonants++;
			}

		}
		vcList.add(vowels);
		vcList.add(consonants);

		return vcList;

	}

}
