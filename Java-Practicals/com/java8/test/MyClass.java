package com.java8.test;

//Example: Default static and void methods

interface MyInterface {

	default void defaultMethod() {
		System.out.println("default method");
	}

	static void staticMethod() {
		System.out.println("static method");
	}

}

public class MyClass implements MyInterface {

	public static void main(String[] args) {

		MyClass obj = new MyClass();
		obj.defaultMethod();
		MyInterface.staticMethod();
	
	}

}
