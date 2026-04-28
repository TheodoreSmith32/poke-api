with sources as (
    select *
    from
    {{source('poke_pg_dbt','pokemon_abilities')}}
)

select distinct
    regexp_replace(language::json ->> 'url', '.*/([0-9]+)/$', '\1')::int as language_id,
    language::json ->> 'name' as language_name
from sources