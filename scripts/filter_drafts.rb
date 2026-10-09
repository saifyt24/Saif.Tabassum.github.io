require "yaml"
require "fileutils"

projects_dir = "_projects"
drafts_dir = ".draft-projects"

FileUtils.mkdir_p(drafts_dir)

Dir.glob(File.join(projects_dir, "*.md")).each do |file|
  content = File.read(file)
  next unless content.start_with?("---\n")

  front_matter = content.split(/^---\s*$\n?/, 3)[1]
  next unless front_matter

  data = YAML.safe_load(front_matter, permitted_classes: [Date, Time], aliases: true) || {}
  next unless data["published"] == false || data["draft"] == true

  FileUtils.mv(file, File.join(drafts_dir, File.basename(file)))
  puts "Excluded draft project: #{File.basename(file)}"
end
