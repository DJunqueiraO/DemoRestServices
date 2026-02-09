package web.djunqueirao.demo_rest_service.adapters.out;

import org.springframework.data.repository.CrudRepository;

import web.djunqueirao.demo_rest_service.domain.Demo;

public interface DemoRepository extends CrudRepository<Demo, Integer> {}