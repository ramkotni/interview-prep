package com.java8.test;

import java.util.Optional;

public class OptionalClass {

	public static void main(String[] args) {

		// Example : Using Optional

		Optional<String> optionalName = Optional.ofNullable(null);
		System.out.println(optionalName.orElse("Default Name"));
		System.out.println("isPresent::"+optionalName.isPresent());
		System.out.println("isEmpty::"+optionalName.isEmpty());

	}

}
