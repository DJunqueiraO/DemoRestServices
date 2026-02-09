package web.djunqueirao.demo_rest_service.application.usecase;

import java.util.Optional;

import org.springframework.stereotype.Service;

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

    public Demo put(Demo demo) {
    	return demoRepositoryPort.save(demo);
    }

    public void delete(Demo demo) {
    	demoRepositoryPort.delete(demo);
    }
}