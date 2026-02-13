package web.djunqueirao.test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

import com.github.djunqueirao.dapi.request.DapiRequestManager;
import com.github.djunqueirao.dapi.request.DapiRequestResponse;

import web.djunqueirao.demo_rest_service.adapters.infraescructure.Jsonable;
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
				.post(endPoint, demo.toJson());
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(201, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should get person")
	void shouldPerformGet() {
		final Demo[] demos = Jsonable.fromJson(new DapiRequestManager(baseUrl).get(endPoint).getBody(), Demo[].class);
		final int id = demos[0].getId();
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.get(endPoint + "/" + id);
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should put person")
	void shouldPerformPut() {
		final Demo[] demos = Jsonable.fromJson(new DapiRequestManager(baseUrl).get(endPoint).getBody(), Demo[].class);
		final int id = demos[0].getId();
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.put(endPoint + "/" + id, demo.setName("test_put").toJson());
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(200, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}

	@Test
	@DisplayName("Should delete person")
	void shouldPerformDelete() {
		final Demo[] demos = Jsonable.fromJson(new DapiRequestManager(baseUrl).get(endPoint).getBody(), Demo[].class);
		final int id = demos[0].getId();
		final DapiRequestResponse persons = new DapiRequestManager(baseUrl)
				.delete(endPoint + "/" + id, demo.toJson());
		Assertions.assertNotNull(persons.getBody());
		Assertions.assertEquals(204, persons.getStatus());
		Assertions.assertNull(persons.getError());
		Assertions.assertNull(persons.getMessage());
	}
}
