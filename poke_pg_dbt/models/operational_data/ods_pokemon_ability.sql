with sources as (
    select *
    from
    {{source('poke_pg_dbt','pokemon_abilities')}}
)

SELECT * FROM Sources