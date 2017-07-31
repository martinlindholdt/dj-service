package dk.tdc.liquid.webservice;

import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(
        plugin = {"pretty","json:target/cucumber.json"},
                glue = {"dk.tdc.liquid.webservice"},
                features = {"src/test/resources/integration"})
public class CucumberIT {}
