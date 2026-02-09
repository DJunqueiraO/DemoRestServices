package web.djunqueirao.demo_rest_service.domain;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import web.djunqueirao.demo_rest_service.adapters.infraescructure.Jsonable;

@Entity
public class Demo implements Jsonable {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;
	private String name;
	
	public int getId() {
		return id;
	}
	
	public String getName() {
		return name;
	}
	
	public Demo setId(int id) {
		this.id = id;
		return this;
	}
	
	public Demo setName(String name) {
		this.name = name;
		return this;
	}
}
