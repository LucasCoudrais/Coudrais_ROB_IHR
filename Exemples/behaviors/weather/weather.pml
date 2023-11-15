<?xml version="1.0" encoding="UTF-8" ?>
<Package name="weather" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="temperature" src="temperature/temperature.dlg" />
    </Dialogs>
    <Resources>
        <File name="" src=".metadata" />
    </Resources>
    <Topics>
        <Topic name="temperature_enu" src="temperature/temperature_enu.top" topicName="temperature" language="en_US" />
        <Topic name="temperature_frf" src="temperature/temperature_frf.top" topicName="temperature" language="fr_FR" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
