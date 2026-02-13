package web.djunqueirao.demo_rest_service.application.usecase;

import java.util.Optional;

import org.springframework.stereotype.Service;

import web.djunqueirao.demo_rest_service.adapters.infraescructure.Jsonable;
import web.djunqueirao.demo_rest_service.application.ports.DemoRepositoryPort;
import web.djunqueirao.demo_rest_service.domain.Demo;

@Service
public class DemoService {

    private final DemoRepositoryPort demoRepositoryPort;

    public DemoService(DemoRepositoryPort repo) {
        this.demoRepositoryPort = repo;
    }

    public Demo post(Demo demo) {
        return demoRepositoryPort.save(demo);
    }

    public Iterable<Demo> getAll() {
        return demoRepositoryPort.findAll();
    }

    public Optional<Demo> get(final int id) {
    	return demoRepositoryPort.findById(id);
    }

    public Demo put(int id, Demo demo) {
    	demo.setId(id);
    	return demoRepositoryPort.save(demo);
    }

    public void delete(int id) {
    	demoRepositoryPort.delete(new Demo().setId(id));
    }
}