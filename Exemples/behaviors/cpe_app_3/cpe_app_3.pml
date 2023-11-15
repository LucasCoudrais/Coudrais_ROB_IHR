<?xml version="1.0" encoding="UTF-8" ?>
<Package name="cpe_app_3" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="phase1" src="phase1/phase1.dlg" />
        <Dialog name="phase2" src="phase2/phase2.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="jquery-1.11.2.min" src="html/jquery-1.11.2.min.js" />
        <File name="sample" src="html/js/sample.js" />
        <File name="sample" src="html/js/sample.js~" />
        <File name="index" src="html/index.html~" />
    </Resources>
    <Topics>
        <Topic name="phase1_enu" src="phase1/phase1_enu.top" topicName="phase1" language="en_US" />
        <Topic name="phase1_frf" src="phase1/phase1_frf.top" topicName="phase1" language="fr_FR" />
        <Topic name="phase2_enu" src="phase2/phase2_enu.top" topicName="phase2" language="en_US" />
        <Topic name="phase2_frf" src="phase2/phase2_frf.top" topicName="phase2" language="fr_FR" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
        <Translation name="translation_fr_FR" src="translations/translation_fr_FR.ts" language="fr_FR" />
    </Translations>
</Package>
