import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_file = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {
        'version':'2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})
    channel_element = xml_tree.SubElement(rss_element, 'channel')
    link_prefix = yaml_file['link']
    xml_tree.SubElement(channel_element, 'title').text = yaml_file['title']    
    xml_tree.SubElement(channel_element, 'format').text = yaml_file['format']    
    xml_tree.SubElement(channel_element, 'subtitle').text = yaml_file['subtitle']    
    xml_tree.SubElement(channel_element, 'version').text = yaml_file['version']    
    xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_file['author']
    xml_tree.SubElement(channel_element, 'description').text = yaml_file['description']
    xml_tree.SubElement(channel_element, 'itunes:image', {'href':link_prefix + yaml_file['image']})
    xml_tree.SubElement(channel_element, 'language').text = yaml_file['language']
    xml_tree.SubElement(channel_element, 'link').text = yaml_file['link']
    xml_tree.SubElement(channel_element, 'itunes:category', {'href':link_prefix + yaml_file['category']})

    for item in yaml_file['item']:
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = item['title']
        xml_tree.SubElement(item_element, 'itunes:author').text = yaml_file['author']
        xml_tree.SubElement(item_element, 'description').text = item['description']
        xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
        xml_tree.SubElement(item_element, 'pubDate').text = item['published']
        enclosure = xml_tree.SubElement(item_element, 'enclosure', {
            'url': link_prefix + item['file'],
            'type': 'audio/mpeg',
            'length': item['length']
        })
    xml_tree.indent(rss_element, space="\t")
    output_tree = xml_tree.ElementTree(rss_element)
    output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)
