package com.java8.test;
@FunctionalInterface
interface MyFunctionalInterface {
    void execute();
    
    default void defaultMethod() {
        System.out.println("Default Method");
    }
    
    static void staticMethod() {
        System.out.println("Static Method");
    }
}

// Using the functional interface with a lambda expression
public class FunctionalInterfaceExample {
    public static void main(String[] args) {
        MyFunctionalInterface func = () -> System.out.println("Executing...");
        func.execute();
    }
}
