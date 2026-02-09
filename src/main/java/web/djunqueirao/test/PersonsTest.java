package web.djunqueirao.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

import com.github.djunqueirao.dapi.request.DapiRequestManager;
import com.github.djunqueirao.dapi.request.DapiRequestResponse;

import web.djunqueirao.demo_rest_service.domain.Demo;


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class PersonsTest {
	
	String baseUrl;
	String endPoint;
	Demo demo;
	
	@BeforeEach
	void BeforeEachTest() {
		this.baseUrl = "http://localhost:8080";
		this.endPoint = "/demos";
		this.demo = new Demo().setName("test");
	}

	@Test
	@DisplayName("Should get all persons")
	void shouldPerformGetAll() {
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl).get(endPoint);
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should post person")
	void shouldPerformPost() {
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.post(endPoint, demo.toString());
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should get person")
	void shouldPerformGet() {
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.get(endPoint + "/1");
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should put person")
	void shouldPerformPut() {
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.put(endPoint, demo.setName("test_put").toString());
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should delete person")
	void shouldPerformDelete() {
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.delete(endPoint, demo.toString());
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}
}
