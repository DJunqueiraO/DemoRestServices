package web.djunqueirao.demo_rest_service.adapters.out;

import java.util.Optional;

import org.springframework.stereotype.Component;

import web.djunqueirao.demo_rest_service.application.ports.DemoRepositoryPort;
import web.djunqueirao.demo_rest_service.domain.Demo;

@Component
public class DemoRepositoryAdapter implements DemoRepositoryPort {

    private final DemoRepository demoRepository;

    public DemoRepositoryAdapter(DemoRepository springRepo) {
        this.demoRepository = springRepo;
    }

    @Override
    public Demo save(Demo demo) {
        return demoRepository.save(demo);
    }

    @Override
    public Iterable<Demo> findAll() {
        return demoRepository.findAll();
    }

    @Override
    public void delete(Demo demo) {
    	demoRepository.delete(demo);
    }

    @Override
    public Optional<Demo> findById(final int id) {
        return demoRepository.findById(id);
    }
}