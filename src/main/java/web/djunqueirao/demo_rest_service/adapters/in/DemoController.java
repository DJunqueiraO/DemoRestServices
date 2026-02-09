package web.djunqueirao.demo_rest_service.adapters.in;

import java.util.Optional;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import web.djunqueirao.demo_rest_service.application.usecase.DemoService;
import web.djunqueirao.demo_rest_service.domain.Demo;

@RestController
@RequestMapping("/demos")
public class DemoController {

    private final DemoService demoService;

    public DemoController(DemoService personService) {
        this.demoService = personService;
    }

    @PostMapping
    public Demo post(@RequestBody Demo person) {
        return demoService.post(person);
    }

    @GetMapping
    public Iterable<Demo> getAll() {
        return demoService.getAll();
    }
    
    @GetMapping("/{id}")
    public Optional<Demo> get(@PathVariable int id) {
        return demoService.get(id);
    }
    
    @DeleteMapping
    public void delete(@RequestBody Demo demo) {
    	demoService.delete(demo);
    }
    
    @PutMapping
    public Demo put(@RequestBody Demo demo) {
        return demoService.put(demo);
    }
}