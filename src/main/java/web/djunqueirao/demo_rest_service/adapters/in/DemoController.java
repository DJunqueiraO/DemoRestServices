package web.djunqueirao.demo_rest_service.adapters.in;

import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
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
	public ResponseEntity<Demo> post(@RequestBody Demo person) {
		final Demo demo = demoService.post(person);
		return ResponseEntity.status(HttpStatus.CREATED).body(demo);
	}

	@GetMapping
	public ResponseEntity<Iterable<Demo>> getAll() {
		final Iterable<Demo> demos = demoService.getAll();
		return ResponseEntity.ok(demos);
	}

	@GetMapping("/{id}")
	public ResponseEntity<Demo> get(@PathVariable int id) {
		return  demoService
				.get(id)
				.map(ResponseEntity::ok)
				.orElse(ResponseEntity.notFound().build());
	}

	@PutMapping("/{id}")
	public ResponseEntity<Demo> put(@PathVariable int id, @RequestBody Demo demo) {
		return ResponseEntity.ok(demoService.put(id, demo));
	}

	@DeleteMapping("/{id}")
	@ResponseStatus(HttpStatus.NO_CONTENT)
	public void delete(@PathVariable int id) {
		demoService.delete(id);
	}
}