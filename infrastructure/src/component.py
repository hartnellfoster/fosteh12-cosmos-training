from BBC.AWS.CloudFormation.Common.Component import Component

component = Component("fosteh12-cosmos-training")
component.set_health_check_url("/status")
component.render()
