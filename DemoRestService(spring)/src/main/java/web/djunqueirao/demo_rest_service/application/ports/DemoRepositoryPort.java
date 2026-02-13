package web.djunqueirao.demo_rest_service.application.ports;

import java.util.Optional;

import web.djunqueirao.demo_rest_service.domain.Demo;

public interface DemoRepositoryPort {
    Demo save(Demo demo);
    Iterable<Demo> findAll();
	void delete(Demo demo);
	Optional<Demo> findById(int id);
}