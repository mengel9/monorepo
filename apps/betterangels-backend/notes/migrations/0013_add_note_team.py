# Generated by Django 5.1.2 on 2024-10-17 00:09

import django_choices_field.fields
import notes.enums
import pgtrigger.compiler
import pgtrigger.migrations
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0012_alter_note_purpose_alter_noteevent_purpose"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="note",
            name="note_add_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="note",
            name="note_update_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="note",
            name="note_remove_delete",
        ),
        migrations.AddField(
            model_name="note",
            name="team",
            field=django_choices_field.fields.TextChoicesField(
                blank=True,
                choices=[
                    ("bowtie_riverside_outreach", "Bowtie & Riverside Outreach"),
                    ("echo_park_on_site", "Echo Park On-site"),
                    ("echo_park_outreach", "Echo Park Outreach"),
                    ("hollywood_on_site", "Hollywood On-site"),
                    ("hollywood_outreach", "Hollywood Outreach"),
                    ("la_river_outreach", "LA River Outreach"),
                    ("los_feliz_outreach", "Los Feliz Outreach"),
                    ("northeast_hollywood_outreach", "Northeast Hollywood Outreach"),
                    ("silver_lake_outreach", "Silver Lake Outreach"),
                    ("slcc_on_site", "SLCC On-site"),
                    ("sunday_social_atwater_on_site", "Sunday Social / Atwater On-site"),
                    ("sunday_social_atwater_outreach", "Sunday Social / Atwater Outreach"),
                    ("wdi_on_site", "WDI On-site"),
                    ("wdi_outreach", "WDI Outreach"),
                ],
                choices_enum=notes.enums.SelahTeamEnum,
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="noteevent",
            name="team",
            field=django_choices_field.fields.TextChoicesField(
                blank=True,
                choices=[
                    ("bowtie_riverside_outreach", "Bowtie & Riverside Outreach"),
                    ("echo_park_on_site", "Echo Park On-site"),
                    ("echo_park_outreach", "Echo Park Outreach"),
                    ("hollywood_on_site", "Hollywood On-site"),
                    ("hollywood_outreach", "Hollywood Outreach"),
                    ("la_river_outreach", "LA River Outreach"),
                    ("los_feliz_outreach", "Los Feliz Outreach"),
                    ("northeast_hollywood_outreach", "Northeast Hollywood Outreach"),
                    ("silver_lake_outreach", "Silver Lake Outreach"),
                    ("slcc_on_site", "SLCC On-site"),
                    ("sunday_social_atwater_on_site", "Sunday Social / Atwater On-site"),
                    ("sunday_social_atwater_outreach", "Sunday Social / Atwater Outreach"),
                    ("wdi_on_site", "WDI On-site"),
                    ("wdi_outreach", "WDI Outreach"),
                ],
                choices_enum=notes.enums.SelahTeamEnum,
                max_length=30,
                null=True,
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="note",
            trigger=pgtrigger.compiler.Trigger(
                name="note_add_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "notes_noteevent" ("client_id", "created_at", "created_by_id", "id", "interacted_at", "is_submitted", "location_id", "organization_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "private_details", "public_details", "purpose", "team", "title", "updated_at") VALUES (NEW."client_id", NEW."created_at", NEW."created_by_id", NEW."id", NEW."interacted_at", NEW."is_submitted", NEW."location_id", NEW."organization_id", _pgh_attach_context(), NOW(), \'note.add\', NEW."id", NEW."private_details", NEW."public_details", NEW."purpose", NEW."team", NEW."title", NEW."updated_at"); RETURN NULL;',
                    hash="feb8b3604bdfd77d7bd956324675e213b7218c85",
                    operation="INSERT",
                    pgid="pgtrigger_note_add_insert_e05e6",
                    table="notes_note",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="note",
            trigger=pgtrigger.compiler.Trigger(
                name="note_update_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition="WHEN (OLD.* IS DISTINCT FROM NEW.*)",
                    func='INSERT INTO "notes_noteevent" ("client_id", "created_at", "created_by_id", "id", "interacted_at", "is_submitted", "location_id", "organization_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "private_details", "public_details", "purpose", "team", "title", "updated_at") VALUES (NEW."client_id", NEW."created_at", NEW."created_by_id", NEW."id", NEW."interacted_at", NEW."is_submitted", NEW."location_id", NEW."organization_id", _pgh_attach_context(), NOW(), \'note.update\', NEW."id", NEW."private_details", NEW."public_details", NEW."purpose", NEW."team", NEW."title", NEW."updated_at"); RETURN NULL;',
                    hash="e77f5fe6685a19a826baab92939d04b219a1c324",
                    operation="UPDATE",
                    pgid="pgtrigger_note_update_update_ac81f",
                    table="notes_note",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="note",
            trigger=pgtrigger.compiler.Trigger(
                name="note_remove_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "notes_noteevent" ("client_id", "created_at", "created_by_id", "id", "interacted_at", "is_submitted", "location_id", "organization_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "private_details", "public_details", "purpose", "team", "title", "updated_at") VALUES (OLD."client_id", OLD."created_at", OLD."created_by_id", OLD."id", OLD."interacted_at", OLD."is_submitted", OLD."location_id", OLD."organization_id", _pgh_attach_context(), NOW(), \'note.remove\', OLD."id", OLD."private_details", OLD."public_details", OLD."purpose", OLD."team", OLD."title", OLD."updated_at"); RETURN NULL;',
                    hash="59a5b9445e553fe6eb6d45d9625de56011df6309",
                    operation="DELETE",
                    pgid="pgtrigger_note_remove_delete_dd722",
                    table="notes_note",
                    when="AFTER",
                ),
            ),
        ),
    ]